import boto3
import botocore
import os
from models import run_data

def getcsvDataS3(file_name: str):
    """
    gets csv data from S3 bucket. 
    returns runData object. 
    modify (try to overload)
    """
    bucket_name = os.getenv('RUNDATA_BUCKET')
    key = 'runDataFiles/{}'.format(file_name)

    s3 = boto3.resource('s3')

    try:
        with open('tempfile', 'wb') as data:
            s3.Bucket(bucket_name).download_fileobj(key, data)
            temp_run_data = run_data.RunData(ioFile=data)
            return temp_run_data
            except botocore.exceptions.ClientError as e:
                if e.response['Error']['Code'] == '404':
                    print("The object does not exist")
                else:
                    raise