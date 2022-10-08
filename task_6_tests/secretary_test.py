import unittest
from unittest.mock import patch
import func_lect2


class TestSecretary(unittest.TestCase):

    @patch('builtins.input')
    def test_find_person(self, user_input):
        user_input.side_effect = ['11-2']
        self.assertEqual(func_lect2.get_doc_owner_name(), None)


    @patch('builtins.input')
    def test_find_shelf(self, user_input):
        user_input.side_effect = ['10006']
        self.assertEqual(func_lect2.get_doc_shelf(), '2')

    @patch('builtins.input')
    def test_add_doc(self, user_input):
        user_input.side_effect = ['10006', 'INN', 'Иван Иванов', '5']
        self.assertEqual(func_lect2.add_new_doc(), '5')

    @patch('builtins.input')
    def test_delete_doc(self, user_input):
        user_input.side_effect = ['11-2']
        self.assertEqual(func_lect2.delete_doc(), ('11-2', True))

    @patch('builtins.input')
    def test_move_doc(self, user_input):
        user_input.side_effect = ['11-2', '3']
        func_lect2.move_doc_to_shelf()
        self.assertEqual(func_lect2.directories['3'], ['11-2'])
