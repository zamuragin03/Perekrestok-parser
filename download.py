import requests


class Downloader:

    def __init__(self, url, method):

        self.url = url
        self.method = method

    def get_html(self):
        response = requests.request(
            method=self.method, url=self.url)
        return response.text

    def save(self, file_path):
        html = self.get_html()
        with open(file_path, "w") as f:
            f.write(html)
