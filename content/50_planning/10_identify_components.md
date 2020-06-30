+++
title = "Identify Quick Start Components"
chapter = false
weight = 10
+++

Now that you have an understanding of architectural best practices, we will break down the Quick Start architecture into smaller components. Think of each components as a Lego peices, which when combined together builds the overall architecture of the Quick Start.

Identifying different components helps us focus on one component at a time when writing the CloudFormation template. 

Each CloudFormation template will focus on just one component. It helps us make our code modular, maintainable and easy to test. 
Also, each component can be developed parallely and put together at the end, to build the overall Quick Start.

Following is the architecture of the Quick Start:
![arch](/images/architecture.png)

Can you identify different components in the above architecture?

{{%expand "Click here to see the list of components" %}}
1. A virtual private cloud (VPC) that spans two Availability Zones, configured with two public and two private subnets. 
2. AWS-managed network address translation (NAT) gateways deployed into the public subnets and configured with an Elastic IP address for outbound internet connectivity.
3. Linux bastion host instances launched in the public subnets, with auto-scaling group enabled.
4. Amazon EC2 web server instances launched in the private subnets, with auto-scaling group enabled.
5. Elastic Load Balancing deployed to automatically distribute traffic across the web server instances.
{{% /expand%}}
