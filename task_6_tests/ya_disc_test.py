import requests
import unittest
from ya_disc_func import YandexFolderCreator


class TestYandexDiskAPI(unittest.TestCase):
    def setUp(self):
        self.uploader = YandexFolderCreator('')

    def test_create_folder(self):
        test_directory = 'Test 1'
        self.assertEqual(self.uploader.create_folder(test_directory).status_code, 201)
        folders_resp = requests.get("https://cloud-api.yandex.net/v1/disk/resources",
                                    params={"path": '/'},
                                    headers={"Authorization": f'OAuth {self.uploader.token}'})

        folders_list = [f['name'] for f in folders_resp.json().get('_embedded').get('items') if f['type'] == 'dir']
        self.assertIn(test_directory, folders_list)

    def tearDown(self):
        del self.uploader