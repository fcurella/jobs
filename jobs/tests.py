from django.test import TestCase
from django.core.urlresolvers import reverse
from jobs.models import Application


class ApplicationTestCase(TestCase):
    fixtures = ['contacts', 'test_data']

    def setUp(self):
        self.application = Application.objects.all()[0]
        self.application.save()  # Generates a new key

    def test_application_detail(self):
        self.assertTrue(self.application.key in self.application.get_absolute_url())

        response = self.client.get(self.application.get_absolute_url())
        self.assertEqual(response.status_code, 200)
