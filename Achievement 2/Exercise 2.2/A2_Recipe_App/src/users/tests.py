from django.test import TestCase

from .models import Users


class UsersModelTest(TestCase):
    def setUpTestData():
        # Set up non-modified objects used by all test methods
        Users.objects.create(name='Narek', password='Hakobyan',
                             email='narek.hakobyan@gmail.com')

    def test_users_name(self):
        # Get a users object to test
        users = Users.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its data
        field_label = users._meta.get_field('name').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'name')

    def test_author_users_max_length(self):
        # Get a users object to test
        users = Users.objects.get(id=1)

        # Get the metadata for the 'author_name' field and use it to query its max_length
        max_length = users._meta.get_field('email').max_length

        # Compare the value to the expected result i.e. 120
        self.assertEqual(max_length, 120)
