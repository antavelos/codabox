from django.core.management.base import BaseCommand, CommandError
from helloworld.models import Entity

class Command(BaseCommand):
    help = 'Shows the Hello <name> message for a given entity_id'

    def add_arguments(self, parser):
        parser.add_argument('entity_id', type=int)

    def handle(self, *args, **options):
        entity_id = options['entity_id']
        try:
            entity = Entity.objects.get(pk=entity_id)
        except Entity.DoesNotExist:
            raise CommandError('Entity with id {} does not exist'.format(entity_id))

        self.stdout.write(self.style.SUCCESS('Hello {}'.format(entity.name)))
