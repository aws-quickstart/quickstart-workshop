# -*- coding: utf-8 -*-
#
# setenv.py
#
# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##################################################################################################

from __future__ import print_function

import time
import boto3
import crhelper


# initialise logger
logger = crhelper.log_config({"RequestId": "CONTAINER_INIT"})
logger.info('Logging configured')
# set global to track init failures
init_failed = False

try:
    # Place initialization code here
    client = boto3.client('ec2')
    logger.info("Container initialization completed")
except Exception as e:
    logger.error(e, exc_info=True)
    init_failed = e


def get_instance(instance_name):
    while True:
        response = client.describe_instances(Filters=[{'Name': 'tag:Name', 'Values': [instance_name]}])
        if len(response['Reservations']) == 1:
            break
        if response['Reservations'][0]['Instances'][0]['State']['Name'] == "running":
            break
        print("instance not stabilised, sleeping 5 seconds and retrying.")
        time.sleep(5)
    return response['Reservations'][0]['Instances'][0]


def attach_role(iam_instance_profile, instance_id):
    client.associate_iam_instance_profile(IamInstanceProfile=iam_instance_profile, InstanceId=instance_id)


def create(event, context):
    """
    Place your code to handle Create events here.

    To return a failure to CloudFormation simply raise an exception, the exception message will be sent to CloudFormation Events.
    """
    physical_resource_id = 'myResourceId'

    print("Received request to {}.".format(event['RequestType']))
    # Open AWS clients

    instance = get_instance('{}{}{}{}'.format('aws-cloud9-', event['ResourceProperties']['StackName'],'-', event['ResourceProperties']['EnvironmentId']))

    instance_name = instance['InstanceId']

    # Get the volume id of the Cloud9 IDE
    block_volume_id = instance['BlockDeviceMappings'][0]['Ebs']['VolumeId']

    # Create the IamInstanceProfile request object
    iam_instance_profile = {
        'Arn': event['ResourceProperties']['C9InstanceProfileArn'],
        'Name': event['ResourceProperties']['C9InstanceProfileName']
    }
    print("Attaching IAM role to instance {}.".format(instance_name))
    attach_role(iam_instance_profile, instance['InstanceId'])

    # Modify the size of the Cloud9 IDE EBS volume
    client.get_waiter('instance_status_ok').wait(InstanceIds=[instance['InstanceId']])
    print("Resizing volume {} for instance {} to {}. This will take several minutes to complete.".format(block_volume_id,instance['InstanceId'],event['ResourceProperties']['EBSVolumeSize']))
    client.modify_volume(VolumeId=block_volume_id,Size=int(event['ResourceProperties']['EBSVolumeSize']))

    # Reboot the Cloud9 IDE
    volume_state = client.describe_volumes_modifications(VolumeIds=[block_volume_id])['VolumesModifications'][0]
    while volume_state['ModificationState'] != 'completed':
        time.sleep(5)
        volume_state = client.describe_volumes_modifications(VolumeIds=[block_volume_id])['VolumesModifications'][0]
    print("Restarting instance {}.".format(instance_name))
    client.reboot_instances(InstanceIds=[instance['InstanceId']])
    response_data = {}
    return physical_resource_id, response_data


def update(event, context):
    """
    Place your code to handle Update events here

    To return a failure to CloudFormation simply raise an exception, the exception message will be sent to CloudFormation Events.
    """
    physical_resource_id = event['PhysicalResourceId']
    response_data = {}
    return physical_resource_id, response_data


def delete(event, context):
    """
    Place your code to handle Delete events here

    To return a failure to CloudFormation simply raise an exception, the exception message will be sent to CloudFormation Events.
    """
    return


def handler(event, context):
    """
    Main handler function, passes off it's work to crhelper's cfn_handler
    """
    # update the logger with event info
    global logger
    logger = crhelper.log_config(event)
    return crhelper.cfn_handler(event, context, create, update, delete, logger, init_failed)
