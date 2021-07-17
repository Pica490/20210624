import unittest
import requests

from unittest.mock import patch
from src.app import get_doc_owner_name, get_all_doc_owners_names, show_all_docs_info, get_doc_shelf, add_new_doc, delete_doc, move_doc_to_shelf, add_new_shelf
from app2 import YandexFolderAdd

def get_input(text):
    return input(text)

class TestSecretaryProgramm(unittest.TestCase):

    @patch('test.get_input', return_value='Василий Гупкин')
    def test_doc_owner(self, input):
        self.assertEqual(get_doc_owner_name(), 'Василий Гупкин')

    @patch('test.get_input', return_value='1')
    def test_doc_shelf(self, input):
        self.assertEqual(get_doc_shelf(), '1')

    @patch('test.get_input', return_value='3')
    def test_add_doc_to_shelf(self, input):
        self.assertEqual(add_new_doc(), '3')

    @patch('test.get_input', return_value='10006')
    def test_delete_doc(self,input):
        self.assertEqual(delete_doc(), ('10006', True))

    @patch('test.get_input', return_value='10006')
    def test_move_doc_to_shelf(self,input):
        self.assertEqual(move_doc_to_shelf(), 'Документ номер "10006" был перемещен на полку номер "3"')

    @patch('test.get_input', return_value='4')
    def test_add_new_shelf(self, input):
        self.assertEqual(add_new_shelf(), ('4', True))

    def test_owner_all_doc_owners(self):
        self.assertEqual({'Аристарх Павлов', 'Василий Гупкин', 'Геннадий Покемонов'}, get_all_doc_owners_names())

    def test_all_docs_info(self):
        self.assertEqual({'name': 'Василий Гупкин', 'number': '2207 876234', 'type': 'passport'}, show_all_docs_info())

class TestYandexFolderAdd(unittest.TestCase):

    def test_add_folder_to_disk(self):
        self.assertEqual(201, YandexFolderAdd.add_folder_to_disk(self))

    @unittest.expectedFailure
    def test_folder_exist(self):
        self.assertEqual(201, YandexFolderAdd.add_folder_to_disk(self))

    def test_find_folder(self):
        url_f = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {'Authorization': ' '}
        params_1 = {'path': 'Photos/'}
        self.assertEqual('Photos', requests.get(url_f, headers = headers, params = params_1).json()['name'])


