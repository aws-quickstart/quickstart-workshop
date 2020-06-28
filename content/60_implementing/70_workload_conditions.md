+++
title = "Workload template - conditions"
chapter = false
weight = 70
+++


Conditions are basically Boolean variables; a condition is either true or false. The “UsingDefaultBucket” condition is “True” if the QSS3BucketName parameter value is “aws-quickstart”, which is the default. This lets us know whether the customer is launching the Quick Start from the AWS Quick Starts public S3 bucket—meaning they likely launched it from the Quick Start landing page—or if they have downloaded the contents of the Quick Start to their own S3 bucket, which customers often do if they want to customize a Quick Start in some way.


	```
	Conditions:
	  UsingDefaultBucket: !Equals [!Ref QSS3BucketName, 'aws-quickstart']
	```

