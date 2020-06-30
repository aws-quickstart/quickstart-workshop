+++
title = "Workload template - mappings"
chapter = false
weight = 60
+++


Next we’ll add the Mappings section of the template. We map an AMI ID for each region to ensure the template launches the correct AMI for the region in which it’s launched.


	```
	Mappings:
	  AWSAMIRegionMap:
	    AMI:
	      AMZNLINUXHVM: amzn-ami-hvm-2018.03.0.20190611-x86_64-gp2
	    ap-northeast-1:
	      AMZNLINUXHVM: ami-02ddf94e5edc8e904
	    ap-northeast-2:
	      AMZNLINUXHVM: ami-0ecd78c22823e02ef
	    ap-south-1:
	      AMZNLINUXHVM: ami-05695932c5299858a
	    ap-southeast-1:
	      AMZNLINUXHVM: ami-043afc2b8b6cfba5c
	    ap-southeast-2:
	      AMZNLINUXHVM: ami-01393ce9a3ca55d67
	    ca-central-1:
	      AMZNLINUXHVM: ami-0fa94ecf2fef3420b
	    eu-central-1:
	      AMZNLINUXHVM: ami-0ba441bdd9e494102
	    eu-west-1:
	      AMZNLINUXHVM: ami-0e61341fa75fcaa18
	    eu-west-2:
	      AMZNLINUXHVM: ami-050b8344d77081f4b
	    sa-east-1:
	      AMZNLINUXHVM: ami-05b7dbc290217250d
	    us-east-1:
	      AMZNLINUXHVM: ami-0e2ff28bfb72a4e45
	    us-east-2:
	      AMZNLINUXHVM: ami-0998bf58313ab53da
	    us-west-1:
	      AMZNLINUXHVM: ami-021bb9f371690f97a
	    us-west-2:
	      AMZNLINUXHVM: ami-079f731edfe27c29c
	```

Alternately, you can run the following command to automatically append the mappings to the file:

```
curl https://raw.githubusercontent.com/aws-quickstart/quickstart-workshop-labs/master/implementing/templates/60_workload_mappings.yaml >> templates/workshop.template.yaml
```