from django.core.management.base import BaseCommand, CommandError
from api.sample import get_source


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)


    def handle(self, *args, **options):

        file_name = options['filename']
        try:
            # import ipdb;ipdb.set_trace()
            get_source(file_name)
        except:
            raise CommandError('invalid file path ')

        print('command started')
        self.stdout.write(self.style.SUCCESS('its working'))
        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()
        #
        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))