import pytz

def say_message(event,context):
    """
    Does a thing

    :param event: An input parameter
    :param context: An input parameter
    :return: Returning value
    """

    if 'message' in event:
        output_text = event['message']
    else:
        output_text = 'Please provide a message to print'
    return {'statusCode': 200, 'Success': True, 'Message': output_text}