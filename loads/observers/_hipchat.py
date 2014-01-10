import logging
import loads
import os
import urllib
import urllib2
import json


def send_message(room, message, notify, color='yellow'):
    token = os.environ['HIPCHAT_TOKEN']
    url = "https://api.hipchat.com/v1/rooms/message"
    values = {
        'auth_token': token,
        'room_id': room,
        'from': 'Loads',
        'message': message,
        'notify': int(notify),
        'color': color,
    }
    data = urllib.urlencode(values)
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    raw_response_data = response.read()
    response_data = json.loads(raw_response_data)
    if 'status' not in response_data:
        logger = logging.getLogger(__name__)
        logger.error('Unexpected response')

    if response_data['status'] != 'sent':
        logger = logging.getLogger(__name__)
        logger.error('Event was not sent to hipchat')


if __name__ == '__main__':
    send_message('Backend', 'ohay, I am the loadzilla bot', False)
