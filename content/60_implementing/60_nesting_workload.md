+++
title = "Creating Workload Stack"
chapter = false
weight = 60
+++

Now you will add **Workload** as a nested stack to your Quick Start. After you have completed the steps listed here, your Quick Start architecture will look like below.

![vpc-bastion](/images/architecture.png)

### Add Workload as a nested stack

Open _templates/master.template.yaml_ in an editor to inspect the contents of the file. You should have only 2 resource - VPCStack and BastionStack.

You will add a resource of Type **‘AWS::CloudFormation::Stack’** to create third nested cloudformation stack.

Close _templates/master.template.yaml_ file and run the following command to add **Workload Stack** resource.

```
curl -s https://raw.githubusercontent.com/aws-quickstart/quickstart-workshop-labs/master/implementing/templates/webserver.master.template.yaml >>templates/master.template.yaml
```

Commit your changes.

` git commit -a -m 'Add Workload as a nested stack'`

### Inspect Workload Stack Resource

Open _templates/master.template.yaml_ in an editor and your **Resources** sections should have WorkloadStack resource, as shown below.

<pre>
	WorkloadStack:
    DependsOn: VPCStack
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL:
        Fn::Sub: https://${QSS3BucketName}.s3.amazonaws.com/${QSS3KeyPrefix}templates/workload.template.yaml
      Parameters:
        EmailAddress:
          Ref: EmailAddress
        InstanceType:
          Ref: InstanceType
        KeyPairName:
          Ref: KeyPairName
        PrivateSubnet1ID:
          Fn::GetAtt:
          - VPCStack
          - Outputs.PrivateSubnet1ID
        PrivateSubnet2ID:
          Fn::GetAtt:
          - VPCStack
          - Outputs.PrivateSubnet2ID
        PublicSubnet1ID:
          Fn::GetAtt:
          - VPCStack
          - Outputs.PublicSubnet1ID
        PublicSubnet2ID:
          Fn::GetAtt:
          - VPCStack
          - Outputs.PublicSubnet2ID
        QSS3BucketName:
          Ref: QSS3BucketName
        QSS3KeyPrefix:
          Ref: QSS3KeyPrefix
        RemoteAccessCIDR:
          Ref: RemoteAccessCIDR
        WebserverCIDR:
          Ref: WebserverCIDR
        VPCID:
          Fn::GetAtt:
          - VPCStack
          - Outputs.VPCID
        VPCIDR:
          Fn::GetAtt:
          - VPCStack
          - Outputs.VPCIDR
</pre>

**Great job!** You have successfully added the Workload to your Quick Start.