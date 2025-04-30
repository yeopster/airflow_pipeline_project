import boto3
import os
import shutil

def download_from_s3():
    local_filename = '/tmp/sales_data.csv'
    try:
        s3 = boto3.client('s3',
                        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                        region_name=os.getenv('AWS_REGION'))

        bucket_name = os.getenv('S3_BUCKET_NAME')
        prefix = os.getenv('S3_KEY_PREFIX')

        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
        objects = response.get('Contents', [])

        if not objects:
            raise Exception("No files found in S3 bucket with prefix.")

        latest_file = sorted(objects, key=lambda obj: obj['LastModified'])[-1]
        file_key = latest_file['Key']


        s3.download_file(bucket_name, file_key, local_filename)
        print(f"Downloaded {file_key} to {local_filename}")
    except Exception as e:
        print("unable to download file from s3", e)
        print("using local file")
        shutil.copy('/opt/airflow/data/sales_data_sample.csv', local_filename)



