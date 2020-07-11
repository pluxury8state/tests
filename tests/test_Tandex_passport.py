from selenium import webdriver
import unittest
import time

class Test_Yandex_passport(unittest.TestCase):

   def setUp(self):

        self.date_to_reg = ['Oleg', 'Popov', 'XDROSE123', 'qwerty12345', '9000000000']
        self.driver = webdriver.Chrome(executable_path = 'C:\\Users\\Олег\\PycharmProjects\\Tests\\Path\\chromedriver.exe')
        self.driver.get('https://passport.yandex.ru/auth/')

   def test_registration(self):
        el1 = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div[2]/a[1]')
        time.sleep(1)
        el1.click()
        self.assertIsNotNone(el1)

   def test_check_form(self):

       # вот тут у меня вопрос: как сделать так , чтобы отработал первый тест и второй запустился на том же месте , где первый закончил работу ?
       # мне это нужно узнать для того , чтобы не переписывать одинаковые строки

       el1 = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div[2]/a[1]')
       time.sleep(1)
       el1.click()



       el_name = self.driver.find_element_by_xpath('//*[@id="firstname"]')
       el_name.click()
       el_name.send_keys(self.date_to_reg[0])
       self.assertEqual(el_name.get_attribute('value'), self.date_to_reg[0])

       el_surname = self.driver.find_element_by_xpath('//*[@id="lastname"]')
       el_surname.send_keys(self.date_to_reg[1])
       self.assertEqual(el_surname.get_attribute('value'), self.date_to_reg[1])

       el_login = self.driver.find_element_by_xpath('//*[@id="login"]')
       el_login.send_keys(self.date_to_reg[2])
       self.assertEqual(el_login.get_attribute('value'), self.date_to_reg[2])

       el_password = self.driver.find_element_by_xpath('//*[@id="password"]')
       el_password.send_keys(self.date_to_reg[3])
       self.assertEqual(el_password.get_attribute('value'), self.date_to_reg[3])

       el_show_password = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/main/div/div/div/form/div[2]/div[1]/button')
       el_show_password.click()
       self.assertIsNotNone(el_show_password)

       el_confirm_password = self.driver.find_element_by_xpath('//*[@id="password_confirm"]')
       el_confirm_password.send_keys(self.date_to_reg[3])
       self.assertEqual(el_confirm_password.get_attribute('value'), self.date_to_reg[3])



       el_telnumber = self.driver.find_element_by_xpath('//*[@id="phone"]')
       if el_telnumber.get_attribute('value') != None:
           el_telnumber.clear()
       el_telnumber.send_keys(self.date_to_reg[4])
       self.assertEqual(el_telnumber.get_attribute('value'), '+7 ' + self.date_to_reg[4])

       el_registraation = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/main/div/div/div/form/div[4]/span/button')
       el_registraation.click()
       self.assertIsNotNone(el_registraation)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Test_Yandex_passport('test_registration'))
    suite.addTest(Test_Yandex_passport('test_check_form'))
    # и тут еще вопрос : почему они запускаются не по порядку?

if __name__ == '__main__':
    runner = unittest.TestRunner()
    runner.run(suite())