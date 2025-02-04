import boto3

s3 = boto3.client('s3')

bucket1 = "manip-project-bucket1"
bucket2 = "manip-project-bucket2"

objects = s3.list_objects_v2(Bucket = bucket1)
for obj in objects.get('Contents',[]):
    file_key = obj['Key']

    copy_source = {'Bucket':bucket1, 'Key':file_key}
    s3.copy_object(CopySource=copy_source, Bucket=bucket2, Key=file_key)

print("All files uploaded and copied successfully")