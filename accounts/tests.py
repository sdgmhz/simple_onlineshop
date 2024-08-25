from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class AccountsAppTests(TestCase):
	username = 'myusername'
	email = 'myusername@gmail.com'

	def test_login_page_by_url(self):
		response = self.client.get('/accounts/login/')
		self.assertEqual(response.status_code, 200)

	def test_login_page_by_name(self):
		response = self.client.get(reverse('login'))
		self.assertEqual(response.status_code, 200)

	def test_login_page_content(self):
		response = self.client.get(reverse('login'))
		self.assertContains(response, 'Log In')

	def test_login_page_template_name(self):
		response = self.client.get(reverse('login'))
		self.assertTemplateUsed(response, 'registration/login.html')

	def test_signup_page_by_url(self):
		response = self.client.get('/accounts/signup/')
		self.assertEqual(response.status_code, 200)

	def test_signup_page_by_name(self):
		response = self.client.get(reverse('signup'))
		self.assertEqual(response.status_code, 200)

	def test_signup_page_content(self):
		response = self.client.get(reverse('signup'))
		self.assertContains(response, 'Sign Up')

	def test_signup_template_name(self):
		response = self.client.get(reverse('signup'))
		self.assertTemplateUsed(response, 'registration/signup.html')

	def test_signup_form(self):
		user = get_user_model().objects.create_user(
			self.username,
			self.email
		)
		self.assertEqual(get_user_model().objects.all().count(), 1)
		self.assertEqual(get_user_model().objects.all()[0].username, self.username)
		self.assertEqual(get_user_model().objects.all()[0].email, self.email)


