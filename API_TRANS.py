import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'



def translate_it(text, to_lang='ru'):

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}'.format(to_lang)
    }
    response = requests.get(URL, params=params)
    json_ = response.json()
    print(type(response))
    return response




if __name__ == '__main__':

    print(translate_it('Hello', 'ru'))
    translate_it('Hello', 'ru')
    translate_it('Hello', 'ru')