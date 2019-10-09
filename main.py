import unittest
from selenium import webdriver


class TestVideo(unittest.TestCase):
    PAGE_URL = 'http://127.0.0.1:8080/'
    # PAGE_URL = 'https://selenium-python.readthedocs.io/'
    WAIT_FOR_FRAME = 2

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.PAGE_URL)

    def tearDown(self):
        self.driver.close()

    def testImg(self):
        'Проверяем, что картинка изменяется со временем'

        img = self.driver.find_element_by_tag_name('img')
        frame1 = img.screenshot_as_png
        self.driver.implicitly_wait(self.WAIT_FOR_FRAME)
        frame2 = img.screenshot_as_png
        assert frame1 != frame2


if __name__ == '__main__':
    unittest.main()
