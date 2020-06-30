+++
title = "Workload template - outputs"
chapter = false
weight = 90
+++


The final section of the Workload template is the Outputs. Once the template has deployed a load balancer in front of an auto scaling group, the customer needs to know the DNS name to use to access their web application; this is displayed in the CloudFormation Outputs tab once the deployment is complete.


	```
	Outputs:
	  ELBDNSName:
	    Description: ELB DNS Name
	    Value:
	      Fn::GetAtt:
	      - ElasticLoadBalancer
	      - DNSName
	```

Alternately, you can run the following command to automatically append the outputs to the file:

```
curl https://raw.githubusercontent.com/aws-quickstart/quickstart-workshop-labs/master/implementing/templates/90_workload_outputs.yaml >> templates/workshop.template.yaml
```