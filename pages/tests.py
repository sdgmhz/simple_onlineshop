from django.test import TestCase
from django.shortcuts import reverse


class TestPagesApp(TestCase):
	# test home page by url
	def test_home_page_by_url(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	# test home page by name
	def test_home_page_by_name(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)

	# test if home page contains "Home Page"
	def test_home_page_content(self):
		response = self.client.get(reverse('home'))
		self.assertContains(response, 'Home Page')

	# test if home page template is 'home.html'
	def test_home_page_template_name(self):
		response = self.client.get(reverse('home'))
		self.assertTemplateUsed(response, 'home.html')

	def test_aboutus_page_by_url(self):
		response = self.client.get('/aboutus/')
		self.assertEqual(response.status_code, 200)

	def test_aboutus_page_by_name(self):
		response = self.client.get(reverse('aboutus'))
		self.assertEqual(response.status_code, 200)

	def test_aboutus_page_content(self):
		response = self.client.get(reverse('aboutus'))
		self.assertContains(response, 'About Us')

	def test_aboutus_page_template_name(self):
		response = self.client.get(reverse('aboutus'))
		self.assertTemplateUsed(response, 'pages/aboutus.html')
