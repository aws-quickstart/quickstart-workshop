+++
title = "Building master template"
chapter = false
weight = 1
+++

{{% notice info %}}
The following instruction must be performed from within your workshop repo **qs-workshop**
{{% /notice %}}

### Deployment options
Each Quick Start should allow users to deploy the workload into an existing VPC and in a new VPC which is created as part of the Quick Start. Which means, you need to provide two deployment options to cover both the scenarios:

1. Building a new virtual private cloud (VPC) that contains the AWS infrastructure for the workload. This scenario enables users to set up a test, demo, or POC environment that doesn’t interfere with their production environment.
2. Deploying the workload into an existing VPC. This scenario enables quick adoption by users who want to deploy the workload into their existing production environment.

### Modularity

To cover both the above scenarios, we will structure our templates in a modular fashion, as shown below.
![master-template](/images/master-template.png?width=60%&height=60%)

**master.template** is the entry point to deploy the Quick Start into a new VPC. It creates a VPC, and the workload, as nested stacks.

**workload.template** is the entry point to deploy the workload into an existing VPC.

To deploy the Quick Start into a new VPC, user will launch **master.template**. And to deploy Quick Start into an already existing VPC, user will launch **workload.template**. Workload template will require VPC information to be passed in as parameters.