import boto3

s3 = boto3.client('s3')

bucket_name = "manip-project-bucket1"

files = ["file1.txt","file2.txt"]

#create sample files
for file in files:
    with open(file, "w") as f:
        f.write(f"This is {file}")

for file in files:
    s3.upload_file(file, bucket_name, file)
    print(f"Uploaded {file} to {bucket_name}")
