from django.test import TestCase
from .models import File

# Create your tests here.
class TestData(TestCase):
	def setUp(self):
		file = File.objects.create(title='Dashain',file_type='Image')


	def test_data(self):
		file = File.objects.get(title='Dashain')
		self.assertEqual(file.title,'Dashain')
		self.assertTrue(file.file_type,'Image')