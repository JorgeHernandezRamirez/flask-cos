import ibm_boto3
from ibm_botocore.client import Config

SERVICE_ENDPOINT = 'https://s3.eu.cloud-object-storage.appdomain.cloud'

def build_cos_client():
    return ibm_boto3.client('s3',
                            config=Config(signature_version='oauth'),
                            endpoint_url=SERVICE_ENDPOINT)

cos = build_cos_client()
