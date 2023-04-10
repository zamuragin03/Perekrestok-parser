from download import Downloader
from parse import Parser
from pathlib import Path
from data import Data
FILE_PATH = "page.html"
path = Path(__file__).parent

def process(URL):
    downloader = Downloader(url=URL, method="GET")
    downloader.save(FILE_PATH)
    parser = Parser(path.joinpath(FILE_PATH))
    parser.save()
    json_file_path = path.joinpath('parse.json')
    data = Data(json_file_path)
    return data.get_avg_data()

if __name__ == '__main__':
    BASE_URL = 'https://www.perekrestok.ru/cat/mc/113/moloko-syr-ajca'
    print(process(BASE_URL))
    