import ibm_boto3
from ibm_botocore.client import Config

AUTH_ENDPOINT = 'https://iam.bluemix.net/oidc/token'
SERVICE_ENDPOINT = 'https://s3-api.us-geo.objectstorage.softlayer.net'

def build_cos_client():
    return ibm_boto3.client('s3',
                            ibm_auth_endpoint=AUTH_ENDPOINT,
                            config=Config(signature_version='oauth'),
                            endpoint_url=SERVICE_ENDPOINT)

cos = build_cos_client()
