import requests


class YaUploader:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def get_files_list(self):

        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'limit': 1, 'media_type': 'image'}
        response = requests.get(url, headers=headers, params=params)

    def get_upload_lint(self, dsik_file_name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': f'/{dsik_file_name}'}
        response = requests.get(url,  headers=self.get_headers(), params=params)
        return response.json()['href']

    def upload(self, file_path, dsik_file_name):
        upload_link = self.get_upload_lint(dsik_file_name)
        response = requests.put(upload_link, headers=self.get_headers(), data=open(file_path, 'rb'))


if __name__ == '__main__':

    path_to_file = 'text_hw.txt'
    token =
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, 'text_hw.txt' )
