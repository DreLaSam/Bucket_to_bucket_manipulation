import boto3

s3 = boto3.client('s3')

def delete_all_objects(bucket_name):
    """Deletes all objects from an S3 bucket."""
    try:
        # List all objects in the bucket
        objects = s3.list_objects_v2(Bucket=bucket_name)

        if 'Contents' in objects:
            # Extract object keys
            object_keys = [{'Key': obj['Key']} for obj in objects['Contents']]

            # Delete objects in bulk
            s3.delete_objects(Bucket=bucket_name, Delete={'Objects': object_keys})
            print(f"Deleted all objects in {bucket_name}")
        else:
            print(f"No objects found in {bucket_name}")

    except Exception as e:
        print(f"Error deleting objects: {e}")

# Replace with your bucket name
bucket_name = "my-resume-project-bucket-1"
delete_all_objects(bucket_name)
