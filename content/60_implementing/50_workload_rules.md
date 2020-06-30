+++
title = "Workload template - rules"
chapter = false
weight = 50
+++


Next, add the Rules section of the template. Rules ensure that the parameter values entered by the customer won’t cause conflicts or stack failures, and prevent the stack from launching if their conditions aren’t met. In this case, we need to ensure that a key pair name has been selected, and that the subnets selected for the deployment are in the same VPC.


	```
	Rules:
	  KeyPairsNotEmpty:
	    Assertions:
	    - Assert:
	        Fn::Not:
	        - Fn::EachMemberEquals:
	          - Fn::RefAll: AWS::EC2::KeyPair::KeyName
	          - ''
	      AssertDescription: All key pair parameters must not be empty
	  SubnetsInVPC:
	    Assertions:
	    - Assert:
	        Fn::EachMemberIn:
	        - Fn::ValueOfAll:
	          - AWS::EC2::Subnet::Id
	          - VpcId
	        - Fn::RefAll: AWS::EC2::VPC::Id
	      AssertDescription: All subnets must in the VPC

	```

Alternately, you can run the following command to automatically append the rules to the file:

```
curl https://raw.githubusercontent.com/aws-quickstart/quickstart-workshop-labs/master/implementing/templates/50_workload_rules.yaml >> templates/workshop.template.yaml
```
