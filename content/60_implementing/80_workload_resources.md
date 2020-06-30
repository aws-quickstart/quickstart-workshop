+++
title = "Workload template - resources"
chapter = false
weight = 80
+++


Go ahead and add the Resources section of the template into your local file. The Resources section is the most important section of the template, since it defines the actual AWS resources that are being deployed. The customer’s selections in the Parameters section are passed to the various resources that are created. Take a look at the highlighted section of the Elastic Load Balancer resource; when the customer selected two subnet IDs during the template deployment, those IDs are passed to the load balancer here. If these two subnet IDs were in different VPCs the load balancer would fail to deploy, which is why we included the rule from the earlier page.


	```
	Resources:
	  NotificationTopic:
	    Type: AWS::SNS::Topic
	    Properties:
	      Subscription:
	      - Endpoint:
	          Ref: OperatorEmail
	        Protocol: email
	  ELBSecurityGroup:
	    Type: AWS::EC2::SecurityGroup
	    Properties:
	      GroupDescription: Allow access to the ELB
	      VpcId:
	        Ref: VPCID
	      SecurityGroupIngress:
	      - IpProtocol: tcp
	        FromPort: '80'
	        ToPort: '80'
	        CidrIp: 0.0.0.0/0
	      - IpProtocol: tcp
	        FromPort: '443'
	        ToPort: '443'
	        CidrIp: 0.0.0.0/0
	  ElasticLoadBalancer:
	    Type: AWS::ElasticLoadBalancing::LoadBalancer
	    Properties:
	      Subnets:
	      - Ref: PublicSubnet1ID
	      - Ref: PublicSubnet2ID
	      SecurityGroups:
	      - Ref: ELBSecurityGroup
	      AppCookieStickinessPolicy:
	      - CookieName: dummy
	        PolicyName: WorkloadCookieStickinessPolicy
	      Listeners:
	      - LoadBalancerPort: '80'
	        InstancePort: '80'
	        Protocol: HTTP
	        PolicyNames:
	        - WorkloadCookieStickinessPolicy
	      CrossZone: 'true'
	      HealthCheck:
	        Target: TCP:80
	        HealthyThreshold: '2'
	        UnhealthyThreshold: '3'
	        Interval: '30'
	        Timeout: '3'
	  SetupRole:
	    Type: AWS::IAM::Role
	    Properties:
	      AssumeRolePolicyDocument:
	        Statement:
	        - Effect: Allow
	          Principal:
	            Service:
	            - ec2.amazonaws.com
	          Action:
	          - sts:AssumeRole
	      Path: /
	      Policies:
	      - PolicyDocument:
	          Version: '2012-10-17'
	          Statement:
	          - Action:
	            - s3:GetObject
	            Resource:
	              - !Sub
	                - arn:${AWS::Partition}:s3:::${S3Bucket}/${QSS3KeyPrefix}*
	                - S3Bucket: !If
	                  - UsingDefaultBucket
	                  - !Sub '${QSS3BucketName}-${AWS::Region}'
	                  - !Ref QSS3BucketName
	            Effect: Allow
	        PolicyName: aws-quick-start-s3-policy
	      - PolicyName: WorkloadSetup
	        PolicyDocument:
	          Statement:
	          - Effect: Allow
	            Action:
	            - cloudwatch:PutMetricData
	            - cloudwatch:EnableAlarmActions
	            - cloudwatch:PutMetricAlarm
	            Resource: '*'
	          - Effect: Allow
	            Action:
	            - s3:*
	            Resource:
	            - Fn::Sub: arn:aws:s3:::${S3Bucket}
	            - Fn::Sub: arn:aws:s3:::${S3Bucket}/*
	  SetupRoleProfile:
	    Type: AWS::IAM::InstanceProfile
	    Properties:
	      Path: /
	      Roles:
	      - Ref: SetupRole
	  WorkloadSecurityGroup:
	    Type: AWS::EC2::SecurityGroup
	    Properties:
	      GroupDescription: Allow access to the Workload instances
	      VpcId:
	        Ref: VPCID
	      SecurityGroupIngress:
	      - IpProtocol: tcp
	        FromPort: '80'
	        ToPort: '80'
	        SourceSecurityGroupId:
	          Ref: ELBSecurityGroup
	      - IpProtocol: tcp
	        FromPort: '443'
	        ToPort: '443'
	        SourceSecurityGroupId:
	          Ref: ELBSecurityGroup
	      - IpProtocol: tcp
	        FromPort: '22'
	        ToPort: '22'
	        SourceSecurityGroupId:
	          Ref: SecurityGroupID
	  WorkloadASLaunchConfig:
	    Type: AWS::AutoScaling::LaunchConfiguration
	    Metadata:
	      AWS::CloudFormation::Init:
	        configSets:
	          quickstart:
	          - install
	          - configure
	          - cleanup
	        install: {}
	        configure: {}
	        cleanup: {}
	    Properties:
	      KeyName:
	        Ref: KeyPairName
	      ImageId:
	        Fn::FindInMap:
	        - AWSAMIRegionMap
	        - Ref: AWS::Region
	        - AMZNLINUXHVM
	      InstanceMonitoring: 'true'
	      IamInstanceProfile:
	        Ref: SetupRoleProfile
	      InstanceType:
	        Ref: WorkloadInstanceType
	      SecurityGroups:
	      - Ref: WorkloadSecurityGroup
	      UserData:
	        Fn::Base64:
	          Fn::Sub: |
	            #!/bin/bash
	            export PATH=$PATH:/usr/local/bin
	            which pip &> /dev/null
	            if [ $? -ne 0 ] ; then
	                echo "PIP NOT INSTALLED"
	                [ `which yum` ] && $(yum install -y epel-release; yum install -y python-pip) && echo "PIP INSTALLED"
	                [ `which apt-get` ] && apt-get -y update && apt-get -y install python-pip && echo "PIP INSTALLED"
	            fi
	            pip install --upgrade pip &> /dev/null
	            pip install awscli --ignore-installed six &> /dev/null
	            easy_install https://s3.amazonaws.com/cloudformation-examples/aws-cfn-bootstrap-latest.tar.gz
	            cfn-init --stack ${AWS::StackName} --resource WorkloadASLaunchConfig --configsets quickstart --region ${AWS::Region}
	            # Signal the status from cfn-init
	            cfn-signal -e $? --stack ${AWS::StackName} --resource WorkloadAutoScalingGroup --region ${AWS::Region}
	  WorkloadScaleUpPolicy:
	    Type: AWS::AutoScaling::ScalingPolicy
	    Properties:
	      AdjustmentType: ChangeInCapacity
	      AutoScalingGroupName:
	        Ref: WorkloadAutoScalingGroup
	      Cooldown: '300'
	      ScalingAdjustment: '1'
	  WorkloadScaleDownPolicy:
	    Type: AWS::AutoScaling::ScalingPolicy
	    Properties:
	      AdjustmentType: ChangeInCapacity
	      AutoScalingGroupName:
	        Ref: WorkloadAutoScalingGroup
	      Cooldown: '300'
	      ScalingAdjustment: '-1'
	  CPUAlarmHigh:
	    Type: AWS::CloudWatch::Alarm
	    Properties:
	      AlarmDescription: Scale-up if CPU > 60% for 5 minutes
	      MetricName: CPUUtilization
	      Namespace: AWS/EC2
	      Statistic: Average
	      Period: '60'
	      EvaluationPeriods: '5'
	      Threshold: '60'
	      AlarmActions:
	      - Ref: WorkloadScaleUpPolicy
	      Dimensions:
	      - Name: AutoScalingGroupName
	        Value:
	          Ref: WorkloadAutoScalingGroup
	      ComparisonOperator: GreaterThanThreshold
	  CPUAlarmLow:
	    Type: AWS::CloudWatch::Alarm
	    Properties:
	      AlarmDescription: Scale-down if CPU < 40% for 30 minutes
	      MetricName: CPUUtilization
	      Namespace: AWS/EC2
	      Statistic: Average
	      Period: '60'
	      EvaluationPeriods: '30'
	      Threshold: '40'
	      AlarmActions:
	      - Ref: WorkloadScaleDownPolicy
	      Dimensions:
	      - Name: AutoScalingGroupName
	        Value:
	          Ref: WorkloadAutoScalingGroup
	      ComparisonOperator: LessThanThreshold
	  WorkloadAutoScalingGroup:
	    Type: AWS::AutoScaling::AutoScalingGroup
	    Properties:
	      VPCZoneIdentifier:
	      - Ref: PrivateSubnet1ID
	      - Ref: PrivateSubnet2ID
	      Cooldown: '600'
	      DesiredCapacity:
	        Ref: WorkloadNodesDesiredCapacity
	      HealthCheckGracePeriod: '600'
	      HealthCheckType: EC2
	      LaunchConfigurationName:
	        Ref: WorkloadASLaunchConfig
	      LoadBalancerNames:
	      - Ref: ElasticLoadBalancer
	      MaxSize:
	        Ref: WorkloadNodesMaxSize
	      MinSize:
	        Ref: WorkloadNodesMinSize
	      NotificationConfiguration:
	        TopicARN:
	          Ref: NotificationTopic
	        NotificationTypes:
	        - autoscaling:EC2_INSTANCE_LAUNCH
	        - autoscaling:EC2_INSTANCE_LAUNCH_ERROR
	        - autoscaling:EC2_INSTANCE_TERMINATE
	        - autoscaling:EC2_INSTANCE_TERMINATE_ERROR
	        - autoscaling:TEST_NOTIFICATION
	      Tags:
	      - Key: Name
	        Value: Workload Server cluster node
	        PropagateAtLaunch: 'true'
	    CreationPolicy:
	      ResourceSignal:
	        Count:
	          Ref: WorkloadNodesDesiredCapacity
	        Timeout: PT2H
	  S3Bucket:
	    Type: AWS::S3::Bucket
	    Properties:
	      BucketName: !Ref 'S3BucketName'
	      AccessControl: BucketOwnerFullControl
	```

Alternately, you can run the following command to automatically append the resources to the file:

```
curl https://raw.githubusercontent.com/aws-quickstart/quickstart-workshop-labs/master/implementing/templates/80_workload_resources.yaml >> templates/workshop.template.yaml
```