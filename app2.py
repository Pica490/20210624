import requests
from pprint import pprint

class YandexFolderAdd:
    def __init__(self):
        self.token = None

    def add_folder_to_disk(self):
        url_f = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {'Authorization': ' '}
        params_1 = {'path': 'Photos/'}
        response = requests.put(url_f, headers=headers, params=params_1)

        return response.status_code

if __name__ == '__main__':
    token = ' '
    result = YandexFolderAdd.add_folder_to_disk(token)