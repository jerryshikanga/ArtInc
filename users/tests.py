from django.test import TestCase
from .models import CustomUser
from django.contrib.auth.models import User
from django.core import mail
from django.test import tag
from selenium.webdriver.chrome.webdriver import WebDriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

# Create your tests here.
class UsersTest(TestCase):
    def setUp(self):
        auth_user = User.objects.create(username="test", password="shikanga")
        # CustomUser.objects.create(user=auth_user, balance=500)
        auth_user.customuser.balance = 500
        auth_user.save()

    @tag('accounts')
    def test_balance_is_updated(self):
        user = User.objects.get(username="test")
        user.customuser.withdraw(100)
        user.refresh_from_db()
        self.assertEqual(int(user.customuser.balance), int(400.00))

    @tag('mailing')
    def test_email(self):
        mail.send_mail(
            'Subject',
            'Message',
            'jerryshikanga@gmail.com',
            [
                'iank299@gmail.com',
                'bianca.mn80@gmail.com',
            ]
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject')

class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ['user-data.json']
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('myuser')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('secret')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
