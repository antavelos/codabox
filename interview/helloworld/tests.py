import sys

from django.test import TestCase
from django.core.management import call_command
from django.core.management.base import CommandError
from django.urls import reverse
from django.utils.six import StringIO
from .models import Entity


def create_entity(name):
    return Entity.objects.create(name=name)


class EntityMethodTests(TestCase):

    def test_entity_detail(self):
        entity = create_entity('test_alex')
        url = reverse('helloworld:detail', args=(entity.id,))
        response = self.client.get(url)
        self.assertContains(response, entity.name)

    def test_entity_detail_404(self):
        url = reverse('helloworld:detail', args=(123456,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_command_output(self):
        entity = create_entity('test_alex')
        out = StringIO()
        call_command('hello_entity', entity.id, stdout=out)
        self.assertIn('Hello {}'.format(entity.name), out.getvalue())

    def test_command_output_does_not_exist(self):
        with self.assertRaises(CommandError):
            call_command('hello_entity', 123456)
