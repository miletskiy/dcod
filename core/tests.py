
from django.test import TestCase
from django.core.urlresolvers import reverse


class CorePageTest(TestCase):
    """
    Test for core view
    """

    def test_core_view(self):
        """
        Core view uses correct template for index page
        and receive correct answer from server
        """
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core.html')
