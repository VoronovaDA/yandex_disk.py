import os
import requests
from settings import token


class YaUploader:
    host = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str):
            self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'} 

 
    def get_upload_link(self, disk_file_name):
        uri = 'v1/disk/resources/upload/'
        url = self.host + uri
        params = {'path': f'/{disk_file_name}'}
        response = requests.get(url, headers=self.get_headers(), params=params)
        return response.json()['href']

    def upload(self, local_file_name, disk_file_name):
        upload_link = self.get_upload_link(disk_file_name)
        response = requests.put(upload_link, headers=self.get_headers(), data=open(local_file_name, 'rb'))
        print(response.status_code)
        if response.status_code == 201:
            print('Загрузка прошла успешно')

if __name__ == '__main__':
    local_file_name = 'homework.json'
    disk_file_name = 'homework.json'
    path = os.getcwd() 
    uploader = YaUploader(token)
    result = uploader.upload(local_file_name, disk_file_name)
 