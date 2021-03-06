
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.management import call_command
from django.core.management.base import CommandError
from core.models import CitiesData
from core.forms import CitiesDataForm


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
        self.assertIsInstance(response.context['form'], CitiesDataForm)


class CommandParseFileTest(TestCase):
    """
    Test for command parsefile
    """

    def test_command_parsefile(self):
        """
        Run command with arg==filename and get the city data in the DB
        """
        self.assertEqual(CitiesData.objects.count(), 0)

        correct_file = '2CuNPefD.csv'
        call_command('parsefile', correct_file)

        self.assertNotEqual(CitiesData.objects.count(), 0)


    def test_command_parsefile_with_wrong_input(self):
        """
        Run command with invalid filename and get the error message
        """
        wrong_file = 'data.txt'

        error_message = 'Please specify only files in CSV format'

        self.assertEqual(CitiesData.objects.count(), 0)

        with self.assertRaises(CommandError) as ce:
            call_command('parsefile', wrong_file)
            self.assertEqual(error_message, ce.exception.message)
