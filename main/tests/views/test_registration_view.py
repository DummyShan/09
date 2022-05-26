from django.test import TestCase

class TestRegistrationView(TestCase):
    def setUp(self):
        # FIRST IS TO COLLECT DATA FROM DATABASE
        # ASSERT DATA ONE BY ONE TO ITS CORRESPONDING COLUMN
        pass

    def test_registered_student_correct(self):
        self.client.post('/', {
            'name': 'Test', 
        })