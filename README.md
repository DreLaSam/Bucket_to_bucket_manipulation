# Bucket_to_bucket_manipulation
This project automates the management of AWS S3 buckets using Python (`boto3`), AWS CLI, and CloudFormation (`YAML`). It follows AWS security best practices by integrating IAM roles and CloudWatch for monitoring.


Project Feautures:
  - Automates S3 bucket creation using create_buckets.py script
  - Automates S3 bucket uploads using upload_files.py script
  - uses CloudFormation to define IaC
  - Monitors file uploads with CloudWatch and SNS email alerts
  - Provides python scripts for file management in S3


Before running project:
  - you will need to have AWS CLI installed and configured
  - you will need to have boto3 installed
        > to do this go on your local terminal and type "pip install boto3"
        > make sure you have permissions to install boto3 on the terminal.



To get the project running:
  Step 1:
    git clone https://github.com/dondre-samuels/aws-s3-automation.git
    cd aws-s3-automation
