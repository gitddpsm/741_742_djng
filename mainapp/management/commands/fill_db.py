from django.core.management.base import BaseCommand
import json
import os

JSON_PATH = 'mainapp/jsons'


def load_from_json(filename):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories
