import boto3

s3 = boto3.client('s3')

def delete_bucket(bucket_name):
    """Deletes an S3 bucket after ensuring it's empty."""
    try:
        # First, delete all objects inside the bucket
        objects = s3.list_objects_v2(Bucket=bucket_name)

        if 'Contents' in objects:
            object_keys = [{'Key': obj['Key']} for obj in objects['Contents']]
            s3.delete_objects(Bucket=bucket_name, Delete={'Objects': object_keys})
            print(f"Deleted all objects in {bucket_name}")

        # Now delete the empty bucket
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Deleted bucket: {bucket_name}")

    except Exception as e:
        print(f"Error deleting bucket: {e}")

# Replace with your bucket name
bucket_name = "my-resume-project-bucket-1"
delete_bucket(bucket_name)
