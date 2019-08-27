import boto3

import log_util


def get_max_data():
    try:
        dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
        table = dynamodb.Table('smartgarden_maxdata')

        response = table.query(KeyConditionExpression='id = :id_smartgarden',
                               ExpressionAttributeValues={
                                   ':id_smartgarden': 'id_smartgarden'},
                               ScanIndexForward=False
                               )

        items = response['Items']

        n = 1  # get latest data
        data = items[:n]
        return data[0]
    except:
        import sys
        log_util.log_error(__name__, sys.exc_info()[0])
        log_util.log_error(__name__, sys.exc_info()[1])


def get_status():
    try:
        dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
        table = dynamodb.Table('smartgarden_status')

        response = table.query(KeyConditionExpression='id = :id_smartgarden',
                               ExpressionAttributeValues={
                                   ':id_smartgarden': 'id_status'
                               },
                               ScanIndexForward=False,
                               Limit=1
                               )

        items = response['Items']

        n = 1
        data = items[:n]
        return data
    except:
        import sys
        log_util.log_error(__name__, sys.exc_info()[0])
        log_util.log_error(__name__, sys.exc_info()[1])
