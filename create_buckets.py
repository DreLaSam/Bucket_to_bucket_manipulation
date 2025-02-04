import boto3


s3 = boto3.client('s3')

bucket1 = "manip-project-bucket1"
bucket2 = "manip-project-bucket2"

#create new s3 buckets
def create_bucket(bucket_name):
    try:
        s3.create_bucket(Bucket = bucket_name)
        print(f"{bucket_name} was created successfully")
    except Exception as e:
        print(f"Error creating bucket {bucket_name}: {e}")


create_bucket(bucket1)
create_bucket(bucket2)

