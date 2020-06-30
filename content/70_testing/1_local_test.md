+++
title = "Testing locally"
chapter = false
weight = 1
+++

At this point, you have all your code built and ready to be tested. We will use TaskCat, an open source tool developed by AWS Quick Start team to simplify and automate the testing of AWS CloudFormation templates. It test the CloudFormation templates by deploying it in multiple AWS Regions simultaneously and generates a report with a pass/fail result for each region. You can customize the tests through a test config file. 

### Create virtual environment

It's a best practice to use virtual environment when working with python projects.

TaskCat requires python3. Therefore, we will create a virtual environment with python3 as default interpreter before installing TaskCat.

Run following commands, to create a virtual environment and use python3 as default interpreter for virtual environment.

```
cd ~/environment/
virtualenv -p /usr/bin/python36 vpy36
source vpy36/bin/activate
```

Run `python --version`, and you should see the output as below:

<pre>
(vpy36) Admin:~/environment $ python --version
Python 3.6.x
</pre>

### Install TaskCat

TaskCat can be installed with Docker or by using pip. We will use pip for this workshop.

From your terminal, run the following command.

`pip install taskcat`

This will install the latest TaskCat version 9.

After the installation is finished, run `taskcat --version` to ensure that TaskCat version 9 is installed correctly.

### Prepare tests

TaskCat requires a project configuration file to configure details about the project and define tests.

This file is created at **\<PROJECT_ROOT\>/.taskcat.yml**.

There are 2 configuration sections in this file as shown below:

1. Project configuration (project)
2. Test configuration (tests)

<pre>
project:
  name: my-cfn-project
  regions:
  - us-west-2
  - eu-north-1
tests:
  default:
    template: ./templates/my-template.yaml
</pre>

#### Project configuration

_project_ section contains the project specific configuration. At minimum, it should have following 2 configurations:

- **name** - Name of the project
- **regions** - List of AWS regions where you want to test your CloudFormation templates

#### Test configuration

_tests_ section is where you define the test related configuration for your project. At minimum, it should have the following:

- **default/template** - path to the template file which needs to be tested, relative to the project config file path.

For the workshop, open the **qs-workshop/.taskcat.yml** file and copy-paste the following contents in it, and save.

```
project:
  name: quickstart-workshop
  owner: quickstart-eng@amazon.com
  package_lambda: false
  regions:
  - us-east-1
  - us-east-2
  - us-west-1
  - us-west-2
  s3_bucket: ''
tests:
  bastion:
    parameters:
      AvailabilityZones: $[taskcat_genaz_2]
      AdminPassword: $[taskcat_genpass_12]
      QSS3BucketName: $[taskcat_autobucket]
      QSS3BucketRegion: $[taskcat_current_region]
      EnvironmentAccessType: Bastion
      KeyPairName: $[taskcat_getkeypair]
      OperatorEmail: test@test.com
      RemoteAccessCIDR: 10.0.4.0/16
      S3BucketName: $[taskcat_random-string]
    regions:
    - us-east-1
    #- us-west-1
    s3_bucket: ''
    template: templates/workshop-master.template.yaml
```

{{% notice tip %}}
TaskCat has several configuration files which can be used to set behaviors in a flexible way and you can read the details in the [TaskCat documentation](https://aws-quickstart.github.io/taskcat/)
{{% /notice %}}

#### Add test parameters

When testing your CloudFormation templates, you need to pass parameter values to use for creating a stack. With TaskCat you can pass these parameter values from configuration file, described above. If you don't specify parameter values in the TaskCat configuration file, you should have default values defined in the template itself for all the parameters.

As you can notice, there are few parameter values which is in the format **$[taskcat_*]**. These are the identifiers which are used to auto-generate the values at runtime by TaskCat. For the complete list of pre-defined identifiers, see the [TaskCat documentation](https://github.com/aws-quickstart/taskcat#more-information-on-taskcat-runtime-injection).

One of these values is **$[taskcat_getkeypair]** for the KeyPairName parameter. You need to replace this with the key pair name of a key pair in your account in us-east-1.


{{%expand "BONUS Section (May be skipped)" %}}

As you can see above, there are few parameters like *KeyPairName* and *EmailAddress* which you may not want to hardcode a value and check it into the github repository. For such situations, TaskCat provide capability to override the project configuration and parameter values via override files. Following are the two override files supported by TaskCat:

- **Project override file** - Place this in the **\<PROJECT-ROOT\>/** directory  
*~/\<PROJECT-ROOT\>/.taskcat_overrides.yml*
- **Global override file** - Place this in the **~/** home directory  
*~/.taskcat.yml*

To understand the precedence of values in different configuration files, read the [Taskcat documentation](https://aws-quickstart.github.io/taskcat/#precedence)

For this workshop, create a project override file and add the parameter values for the Email address and Key pair name. Your file should look like below:

```
EmailAddress: email@yourdomain.com
KeyPairName: YOUR-KEYPAIR-HERE
```
{{% /expand%}}

### Running tests

Now that we have taskcat configuration file created, let's run TaskCat to execute our tests.

Run the following command in your terminal window:

`cd ~/environment/qs-workshop`

`taskcat test run -l &> screen-logs.txt &`

This will run TaskCat in the background and send logs/errors to *screen-logs.txt* file. TaskCat performs series of actions as part of executing a test, such as template validation, parameter validation, staging content into S3 bucket, and launching CloudFormation stack. It launches the stack creation in all the defined regions, for each test, simultaneously. And regularly polls the CloudFormation stack status to check if the stack creation is finished. How much time TaskCat takes to finish the testing, depends on how many tests you have defined in your TaskCat configuration file and how long each stack creation and deletion takes.

You can *tail* the logs by running following command.

`tail -f screen-logs.txt`

After the TaskCat run is complete, you will see a report genereated in HTML format in the current directory from where you are running TaskCat command. You can see the report by *right click* on **taskcat_outputs/index.html**, and click *preview*. Your report should look like below:

![taskcat-report](/images/taskcat-report.png)

If you do not see all green, you can click on the **View Logs** link for the failed test and see the CloudFormation event logs for further troubleshooting.
