+++
title = "Adding submodules"
chapter = false
weight = 10
+++

The Quick Start catalog has **170+** Quick Starts. It includes a [VPC Quick Start](https://aws.amazon.com/quickstart/architecture/vpc/) which builds a virtual private network (VPC) environment with public and private subnets, following AWS best practices. It also includes [Linux Bastion](https://aws.amazon.com/quickstart/architecture/linux-bastion/) and [Microsoft Remote Desktop Gateway](https://aws.amazon.com/quickstart/architecture/rd-gateway/) Quick Starts that allow users to access assets in private subnets via bastion hosts.

You will use the VPC Quick Start to create a VPC in your workshop Quick Start, and the Bastion Quick Starts to allow remote access to the solution. By using existing Quick Starts, you get the following benefits:

- Re-use the architeture built by AWS SAs, which follows the AWS best practices.
- Automatically get the AMI and security updates for VPC and Linux bastion stacks.
- Less code to maintain.
- Focus on building the workload.
- Avoid duplicating same code across multiple Quick Starts

### Git Submodules
To use these existing Quick Starts in your workshop Quick Start, you will use Git Submodules.

Git Submodules allow you to keep a Git repository as a subdirectory of another Git repository. This lets you clone another repository into your project and keep your commits separate.

We will add submodules to the **qs-workshop** repo - QuickStart VPC, Linux Bastion, and Remote Desktop Gateway.

### Add submodules to your project
Change directory to the root of your repo.

Make sure you are in *qs-workshop* folder.

Add submodules.

```
git submodule add -b master https://github.com/aws-quickstart/quickstart-aws-vpc.git submodules/quickstart-aws-vpc
git submodule add -b master https://github.com/aws-quickstart/quickstart-linux-bastion.git submodules/quickstart-linux-bastion
git submodule add -b master https://github.com/aws-quickstart/quickstart-microsoft-rdgateway.git submodules/quickstart-microsoft-rdgateway
git submodule update --init --recursive

```

By running the above commands, you have added the **quickstart-aws-vpc**, **quickstart-linux-bastion**, and **quickstart-microsoft-rdgateway** git repositories as submodules in the **submodules/** directory of qs-workshop repo, and the submodules are tracking the master branch of their respective repositories.

Now, Commit your changes and push to the develop branch.

`git commit -a -m "Add QuickStart VPC Submodule"`

{{% notice tip %}}
If you need to update your submodules later you can use the following command  `git submodule update --recursive`
Similarly, if you are cloning an existing repo that already contains a submodule you will need to run `git submodule init` first, then `git submodule update -r` after to copy the contents.
{{% /notice %}}

### Verify project structure

Your project directory **qs-workshop** should look like below.

<pre>

    ├── .git
    ├── docs
    ├── submodules
    │   └── quickstart-aws-vpc
    │   └── quickstart-linux-bastion
    │   └── quickstart-microsoft-rdgateway
    ├── templates
    │   └── workshop.template.yaml
    │   └── workshop-master.template.yaml
    ├── .gitmodules
    └── .taskcat.yml
</pre>

Once you have verified that your project structure is correct, its time to push the changes to the develop branch.

Run `git push origin develop`

<pre>
    Enumerating objects: 13, done.
    Counting objects: 100% (13/13), done.
    Delta compression using up to 8 threads
    Compressing objects: 100% (8/8), done.
    Writing objects: 100% (8/8), 1.86 KiB | 635.00 KiB/s, done.
    Total 8 (delta 1), reused 0 (delta 0)
    remote: Resolving deltas: 100% (1/1), completed with 1 local object.
    To github.com:avattathil/qs-workshop.git
       3fe60df..acdba90  develop -> develop
</pre>
