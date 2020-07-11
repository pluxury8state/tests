import unittest
import app
from unittest.mock import patch
from fixtures.documents import documents
from fixtures.directiries import directories

class Secretary_Tests(unittest.TestCase):

    def setUp(self):
        self.documents = documents
        self.directories = directories
        with patch('app.update_date', return_value=(self.directories, self.documents)):
            with patch('app.input', return_value='q'):
                app.secretary_program_start()



    def test_add_new_document(self):
        self.assertNotIn('113', app.directories['3'])
        with patch('app.input', side_effect=['113', 'pas', 'Rick', '3']):
            app.add_new_doc()
        self.assertIn('113', app.directories['3'])

    def test_remove_document(self):
        self.assertIn('10006', app.directories['2'])
        with patch('app.input', return_value='10006'):
            app.delete_doc()
        self.assertNotIn('10006', app.directories['2'])

    def test_show_info(self):
        app.show_all_docs_info()
