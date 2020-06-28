+++
title = "Workload template - parameters"
chapter = false
weight = 40
+++


The Parameters section of the template includes all of the parameters that will be used to define the resources in the stack. For example, since this workload template will be deploying an EC2 auto scaling group across two Availability Zones, we need to enter the subnet IDs of the two subnets in which the instances will be deployed. Likewise, we need to define the ID of the VPC in which these subnets reside; we need to define the instance type for the EC2 instances, etc. Where possible we try to set default values for parameters, which limits the number of items a customer has to manually enter or select when launching the template.


	```
	Parameters:
	  SecurityGroupID:
	    Description: ID of the security group to enable SSH/RDGW connections (e.g.,
	      sg-7f16e910).
	    Type: AWS::EC2::SecurityGroup::Id
	  KeyPairName:
	    Description: Name of an existing EC2 key pair. All instances will launch with
	      this key pair.
	    Type: AWS::EC2::KeyPair::KeyName
	  OperatorEmail:
	    AllowedPattern: ([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)
	    ConstraintDescription: Must be a valid email address.
	    Description: Email address that notifications of any scaling operations will be
	      sent to.
	    Type: String
	  PrivateSubnet1ID:
	    Description: ID of private subnet 1 in Availability Zone 1 for the workload (e.g.,
	      subnet-a0246dcd).
	    Type: AWS::EC2::Subnet::Id
	  PrivateSubnet2ID:
	    Description: ID of private subnet 2 in Availability Zone 2 for the workload (e.g.,
	      subnet-b1f432cd).
	    Type: AWS::EC2::Subnet::Id
	  PublicSubnet1ID:
	    Description: ID of public subnet 1 in Availability Zone 1 for the ELB load balancer
	      (e.g., subnet-9bc642ac).
	    Type: AWS::EC2::Subnet::Id
	  PublicSubnet2ID:
	    Description: ID of public subnet 2 in Availability Zone 2 for the ELB load balancer
	      (e.g., subnet-e3246d8e).
	    Type: AWS::EC2::Subnet::Id
	  QSS3BucketName:
	    AllowedPattern: ^[0-9a-zA-Z]+([0-9a-zA-Z-]*[0-9a-zA-Z])*$
	    ConstraintDescription: Quick Start bucket name can include numbers, lowercase
	      letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen
	      (-).
	    Default: aws-quickstart
	    Description: S3 bucket name for the Quick Start assets. This string can include
	      numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start
	      or end with a hyphen (-).
	    Type: String
	  QSS3BucketRegion:
	    Default: 'us-east-1'
	    Description: 'The AWS Region where the Quick Start S3 bucket (QSS3BucketName) is hosted. When using your own bucket, you must specify this value.'
	    Type: String
	  QSS3KeyPrefix:
	    AllowedPattern: ^[0-9a-zA-Z-/]*$
	    ConstraintDescription: Quick Start key prefix can include numbers, lowercase letters,
	      uppercase letters, hyphens (-), and forward slash (/).
	    Default: quickstart-workshop/
	    Description: S3 key prefix for the Quick Start assets. Quick Start key prefix
	      can include numbers, lowercase letters, uppercase letters, hyphens (-), and
	      forward slash (/).
	    Type: String
	  S3BucketName:
	    AllowedPattern: ^[a-z0-9][a-z0-9-.]*$
	    Description: Name of the S3 bucket that will be created for your workload to store
	      data. Enter a unique name that does not include uppercase characters.
	    Type: String
	  VPCID:
	    Description: ID of your existing VPC for deployment.
	    Type: AWS::EC2::VPC::Id
	  WorkloadInstanceType:
	    AllowedValues:
	    - t2.large
	    - m4.large
	    - m4.xlarge
	    - m4.2xlarge
	    - m4.4xlarge
	    - m4.10xlarge
	    - m3.medium
	    - m3.large
	    - m3.xlarge
	    - m3.2xlarge
	    - c4.large
	    - c4.xlarge
	    - c4.2xlarge
	    - c4.4xlarge
	    - c4.8xlarge
	    - c3.large
	    - c3.xlarge
	    - c3.2xlarge
	    - c3.4xlarge
	    - c3.8xlarge
	    - r3.large
	    - r3.xlarge
	    ConstraintDescription: Must contain valid instance type
	    Default: m4.xlarge
	    Description: Type of EC2 instance for the workload instances.
	    Type: String
	  WorkloadNodesDesiredCapacity:
	    Default: '2'
	    Description: Desired capacity for the workload nodes Auto Scaling group.
	    Type: String
	  WorkloadNodesMaxSize:
	    Default: '4'
	    Description: Maximum size of the Auto Scaling group.
	    Type: String
	  WorkloadNodesMinSize:
	    Default: '2'
	    Description: Minimum size of the Auto Scaling group.
	    Type: String
	```

