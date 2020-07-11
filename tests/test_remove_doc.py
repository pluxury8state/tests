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

    def test_remove_document(self):
        self.assertIn('10006', app.directories['2'])
        with patch('app.input', return_value='10006'):
            app.delete_doc()
        self.assertNotIn('10006', app.directories['2'])
