from django.test import TestCase

from .models import Recipes


class RecipeModelTest(TestCase):
    def setUpTestData():
        # Set up non-modified objects used by all test methods
        Recipes.objects.create(name='Pizza', difficulty='Hard',
                               adapted='BBC', adapted_link='BBC.com', description='Mom\'s pizza pie',
                               prepTime=20, cookTime=30, totalTime=50, serving=3,
                               ingredients='dough, chees, sauce, pepperoni')

    def test_recipes_name(self):
        # Get a users object to test
        users = Recipes.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its data
        field_label = users._meta.get_field('name').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'name')

    def test_recepies_name_max_length(self):
        # Get a users object to test
        users = Recipes.objects.get(id=1)

        # Get the metadata for the 'author_name' field and use it to query its max_length
        max_length = users._meta.get_field('name').max_length

        # Compare the value to the expected result i.e. 120
        self.assertEqual(max_length, 120)
