from requests import get
import unittest
from requests import get
from unittest.mock import patch
import API_TRANS

class Test_API_Yandex(unittest.TestCase):

    def setUp(self):
        self.text = 'Hello'
        self.lang = 'ru'
        self.Url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

        self.params = {
            'key': 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0',
            'text': self.text,
            'lang': '{}'.format(self.lang)
        }


    def test_succesful_connetion(self):
        obj = str(get(self.Url,self.params))
        self.assertEqual(obj,'<Response [200]>')
    # у меня вот тут вопрос , а можно ли как-нибудь сравнить эти два значения , но не использовать строки?

    def test_true_text(self):
        obj = get(self.Url, self.params).json()['text']
        self.assertEqual(obj, ['Привет'])
