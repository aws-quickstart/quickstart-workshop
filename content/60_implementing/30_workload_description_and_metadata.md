+++
title = "Workload template - description and metadata"
chapter = false
weight = 30
+++


We will start by building the workload template. This deploys the actual workload that the Quick Start is being designed to deploy. Double-click “workshop-workload.template.yaml” in your IDE to open the file, and paste the description and metadata sections of the template (see below). The description section simply describes what the Quick Start will deploy. The ParameterGroups metadata section defines the order and grouping with which CloudFormation parameters will be displayed to the customer, and the ParameterLabels metadata section provides descriptive labels for the template’s parameters, which can sometimes have obscure names.

	```
	AWSTemplateFormatVersion: '2010-09-09'
	Description: This workload template deploys an ASG behind an ELB load balancer in
	  two private subnets. The cluster is configured to use an S3 bucket for storage **WARNING**
	  This template creates EC2 instances and related resources. You will be billed for
	  the AWS resources used if you create a stack from this template.
	Metadata:
	  AWS::CloudFormation::Interface:
	    ParameterGroups:
	    - Label:
	        default: Network configuration
	      Parameters:
	      - VPCID
	      - PrivateSubnet1ID
	      - PrivateSubnet2ID
	      - PublicSubnet1ID
	      - PublicSubnet2ID
	    - Label:
	        default: Amazon EC2 configuration
	      Parameters:
	      - KeyPairName
	      - BastionSecurityGroupID
	      - WorkloadInstanceType
	    - Label:
	        default: Workload nodes configuration
	      Parameters:
	      - WorkloadNodesMinSize
	      - WorkloadNodesMaxSize
	      - WorkloadNodesDesiredCapacity
	      - OperatorEmail
	    - Label:
	        default: Workload storage configuration
	      Parameters:
	      - S3BucketName
	    - Label:
	        default: AWS Quick Start configuration
	      Parameters:
	      - QSS3BucketName
	      - QSS3BucketRegion
	      - QSS3KeyPrefix
	    ParameterLabels:
	      BastionSecurityGroupID:
	        default: Bastion security group ID
	      KeyPairName:
	        default: SSH key name
	      OperatorEmail:
	        default: Operator email
	      PrivateSubnet1ID:
	        default: Private subnet 1 ID
	      PrivateSubnet2ID:
	        default: Private subnet 2 ID
	      PublicSubnet1ID:
	        default: Public subnet 1 ID
	      PublicSubnet2ID:
	        default: Public subnet 2 ID
	      QSS3BucketName:
	        default: Quick Start S3 bucket name
	      QSS3BucketRegion:
	        default: Quick Start S3 bucket region
	      QSS3KeyPrefix:
	        default: Quick Start S3 key prefix
	      S3BucketName:
	        default: S3 bucket name
	      VPCID:
	        default: VPC ID
	      WorkloadInstanceType:
	        default: Workload servers instance type
	      WorkloadNodesDesiredCapacity:
	        default: Workload nodes desired capacity
	      WorkloadNodesMaxSize:
	        default: Workload nodes max size
	      WorkloadNodesMinSize:
	        default: Workload nodes min size
	```

