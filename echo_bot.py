from dotenv import load_dotenv
import os
import time
import requests

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

BASE_URL = f'https://api.telegram.org/bot{TOKEN}'


def get_update(offset):
    url = BASE_URL + '/getUpdates'
    params = {'timeout': 100, 'allowed_updates': ['message']}
    if offset:
        params['offset'] = offset
    try:
        response = requests.get(url=url, params=params)
    except requests.exceptions.RequestException as e:
        print(f'Error in get_update: {e}')
    return response.json()


def send_message(chat_id, text):
    url = BASE_URL + '/sendMessage'
    params = {'chat_id': chat_id, 'text': text}
    try:
        response = requests.post(url=url, params=params)
    except requests.exceptions.RequestException as e:
        print(f'Error in send_message: {e}')
    return response.json()


def main():
    print('start bot ...')
    offset = None

    while True:
        try:
            updates = get_update(offset=offset)
            if 'result' in updates:
                for update in updates['result']:
                    offset = update['update_id'] + 1
                    if 'message' in update and 'text' in update['message']:
                        chat_id = update['message']['chat']['id']
                        text = update['message']['text']
                        print(f'chat id: {chat_id}, text: {text}')

                        response = send_message(chat_id=chat_id, text=f'you said: {text}')

            time.sleep(1)
        except Exception as e:
            print('Error in main: {e}')
            time.sleep(5)


if __name__ == '__main__':
    main()
