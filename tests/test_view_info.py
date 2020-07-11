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

    def test_show_info(self):
        app.show_all_docs_info()