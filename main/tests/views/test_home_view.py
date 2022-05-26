from django.test import TestCase
from django.urls import reverse

class TestHomeView(TestCase):
    response = None

    def setUp(self):
        self.response = self.client.get('/')

    def test_view_url_exists_at_desired_enpoint(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_view_if_used_correct_template(self):
        self.assertTemplateUsed(self.response, 'main/home.html')
    
    def test_view_if_accessible_by_name(self):
        response = self.client.get(reverse('stsm-home'))
        self.assertEqual(response.status_code, 200)