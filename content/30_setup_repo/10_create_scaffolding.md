+++
title = "Create Scaffolding"
chapter = false
weight = 20
+++

The GitHub repository for each Quick Start includes the following folders:

- **docs** - (optional) Contains the Quick Start documentation
- **templates** - (required) Contains the AWS CloudFormation templates for the Quick Start. All templates use the .template file extension.
- **scripts** - (optional) Contains the scripts and configuration files that are used in the Quick Start; for example, to orchestrate the bootstrap, install or configure an app, or update a host.
- **functions** - (optional) Contains lambda functions used in the Quick Start.
- **submodules** - (optional) Used for any referenced Quick Starts that are configured as submodules of the Quick Start. These follow the naming convention _/submodules/quickstart-repo-name_ where the contents are synced at a specific commit level.

Do not worry if some of the folders described above doesn't make sense, yet. As you follow along the rest of the workshop, things will get more clear.

### Copy repo URL

Copy the url of your github repo
![repo url](/images/copy-qs-workshop-path.png)

### Clone repo

Clone the repo by running the following command. Replace *GITHUB_REPO_URL* with your url.

`git clone GITHUB_REPO_URL`

You should see following output.
<pre>
Admin:~/environment $ git clone https://github.com/davmayd2/qs-workshop.git
Cloning into 'qs-workshop'...
warning: You appear to have cloned an empty repository.
</pre>

{{%expand "Click here if you get an error" %}}
#### Error: Permission denied (publickey)
<pre>
Admin:~/environment $ git clone git@github.com:sshvans/qs-workshop.git
Cloning into 'qs-workshop'...
The authenticity of host 'github.com (192.30.253.112)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
RSA key fingerprint is MD5:16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,192.30.253.112' (RSA) to the list of known hosts.
Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
</pre>

If you see above error message, it means you are using SSH URL to clone the repository, and you don't have SSH private key setup on your development environment machine.

To quick fix the issue, run `git clone GITHUB_REPO_URL` with HTTPS URL of your GitHub repo. 

{{% /expand%}}

### Create scaffolding
When a Quick Start repo is created by the Quick Start team, all the folders are pre-created for you. But, as you are creating your own repo for this workshop, you need to create necessary folders.

1. In your IDE's terminal window, navigate to the repository

 	`cd qs-workshop`

2. Create the necessary subdirectories

	```
	mkdir docs
	mkdir submodules
	mkdir templates
	```

3. Create the necessary files

	```
	echo > .taskcat.yml
	echo > templates/workshop.template.yaml
	echo > templates/workshop-master.template.yaml
	```

3. Add and Commit your changes

	`git add --all .`

	`git commit -a -m 'Load base content'`
	
	You should see the following output.
	
	<pre>
	[master (root-commit) ab0660b] Load base content
	 	 3 files changed, 3 insertions(+)
		 create mode 100644 .taskcat.yml
		 create mode 100644 templates/workshop.template.yaml
		 create mode 100644 templates/workshop-master.template.yaml
	</pre>

4. Now that you have your changes committed locally to your repo, we will push these changes to github remote master branch.

	`git push`
	
	You should see the following output.
	
	<pre>
	Enumerating objects: 7, done.
	Counting objects: 100% (7/7), done.
	Delta compression using up to 8 threads
	Compressing objects: 100% (6/6), done.
	Writing objects: 100% (7/7), 753 bytes | 753.00 KiB/s, done.
	Total 7 (delta 0), reused 0 (delta 0)
	To github.com:avattathil/qs-workshop.git
	** [new branch]      master -> master
	</pre>

{{%expand "Click here if your output doesn't match above" %}}
#### Prompt: Enter github username
<pre>
Admin:~/environment/qs-workshop (master) $ git push
Username for 'https://github.com':
</pre>

Don't worry if you see the above prompt. It's asking you to enter the github username and password to authenticate your git action. You see this prompt because you are doing *git push* for the first time. Here onwards, Git has cached your credentials in memory for the time period specified in [Setup Git CLI](/10_prerequisites/40_setup_github_cli.html#configure-git-credentials) step. 

Enter your github username and personal token (for password) to push the changes. Your output should look like following:

<pre>
Admin:~/environment/qs-workshop (master) $ git push
Username for 'https://github.com': sshvans
Password for 'https://sshvans@github.com': 
Counting objects: 7, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (6/6), done.
Writing objects: 100% (7/7), 830 bytes | 830.00 KiB/s, done.
Total 7 (delta 0), reused 0 (delta 0)
To https://github.com/sshvans/qs-workshop.git
 * [new branch]      master -> master
</pre>
{{% /expand%}}

### Create development branch

When you create a GitHub repository, it only contains **master** branch. 

As a best practice, you should keep the development and release branches separate. We will use **develop** branch for development and **master** branch for releases of the Quick Start. 

![git branches](/images/git-branches.png?height=50%&width=50%)

Currently, we only have _master_ branch in our github repo. So, let's create a _develop_ branch from the _master_ branch.

1. Create and checkout develop branch from master

	`git checkout -b develop`

2. Push develop branch to remote and set the upstream

	`git push --set-upstream origin develop`
	
	Your  output should look like below:

	<pre>
	Warning: Permanently added the RSA host key for IP address '192.30.253.113' to the list of known hosts.
	Total 0 (delta 0), reused 0 (delta 0)
	remote:
	remote: Create a pull request for 'develop' on GitHub by visiting:
	remote:      https://github.com/avattathil/qs-workshop/pull/new/develop
	remote:
	To github.com:avattathil/qs-workshop.git
	** [new branch]      develop -> develop
	Branch 'develop' set up to track remote branch 'develop' from 'origin'.
	</pre>


