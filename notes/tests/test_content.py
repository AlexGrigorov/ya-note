from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from notes.models import Note

User = get_user_model()


class TestListPage(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(username='Лев Толстой')
        cls.reader = User.objects.create(username='Читатель')
        cls.reader_client = Client()
        cls.reader_client.force_login(cls.reader)
        all_notes = [
            Note(
                title=f'Заголовок{index}',
                text='Текст.',
                author=cls.author,
                slug=f'{index}'
            )
            for index in range(10)
        ]
        Note.objects.bulk_create(all_notes)

    def test_single_note(self):
        self.client.force_login(self.author)
        url = reverse('notes:list')
        response = self.client.get(url)
        object_list = response.context['object_list']
        self.assertIn(object_list[0], object_list)

    def test_author_list_of_notes(self):
        self.client.force_login(self.author)
        url = reverse('notes:list')
        response = self.client.get(url)
        object_list = response.context['object_list']
        notes = len(object_list)
        self.assertEqual(notes, 10)

    def test_reader_list_of_notes(self):
        self.client.force_login(self.reader)
        url = reverse('notes:list')
        response = self.client.get(url)
        object_list = response.context['object_list']
        notes = len(object_list)
        self.assertEqual(notes, 0)


class TestAddEddPage(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(username='Лев Толстой')
        cls.notes = Note.objects.create(
            title='Заголовок',
            text='Текст',
            author=cls.author
        )

    def test_add_form(self):
        self.client.force_login(self.author)
        url = reverse('notes:add')
        response = self.client.get(url)
        self.assertIn('form', response.context)

    def test_editt_form(self):
        self.client.force_login(self.author)
        url = reverse('notes:edit', args=(self.notes.slug,))
        response = self.client.get(url)
        self.assertIn('form', response.context)
