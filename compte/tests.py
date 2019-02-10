from django.test import TestCase
from django.urls import reverse
from .models import User
from django.contrib.auth import authenticate

class IndexPageTestCase(TestCase):

    def test_index_page(self):

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_index_page_contain(self):

        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Colette et Remy</h2>')

# Create your tests here.


class PasswordOkTestCase(TestCase):

    # test that detail page returns a 200 if the item exists.
    def test_detail_page_returns_200(self):
        self.new_user = User.objects.create_user('manu@hotmail.com','','salut')
        self.new_user.save()

        self.user = authenticate(username='manu@hotmail.com',
                            password='salut')  # Nous vérifions si les données sont correctes

        #if self.user is not None:
        if self.user:
            authenticated = 'yes'
        else:
            authenticated = 'no'

        self.assertEqual(authenticated, 'yes')

    def PasswordNokTestCase(self):
        self.new_user = User.objects.create_user('manu@hotmail.com', '', 'salut')
        self.new_user.save()

        self.user = authenticate(username='manu@hotmail.com',
                                 password='sal')  # Nous vérifions si les données sont correctes

        # if self.user is not None:
        if self.user:
            authenticated = 'yes'
        else:
            authenticated = 'no'

        self.assertEqual(authenticated, 'no')

        #https://wsvincent.com/django-testing-tutorial/



        #utilisateur mauvais
        #utilisateur existe deja


