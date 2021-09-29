import pytz

def say_message(event,context):
    """
    Does a thing

    :param event: An input parameter
    :param context: An input parameter
    :return: Returning value
    """
    print("Message is:",event['message'])
    return {'StatusCode': 200, 'Success': True, 'Message': event['message']}