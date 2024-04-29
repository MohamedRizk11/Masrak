'''import json
from django.core.management.base import BaseCommand
from masark.models import Station'''

from django.core.management.base import BaseCommand
import json

class Command(BaseCommand):
    help = 'Import external JSON File data into Django database'

    def handle(self, *args, **kwargs):
        with open(r'D:\course python\masark\src\project\station.json', 'r', encoding='utf8') as file:
            data = json.load(file)
            print(data)

'''
            # Iterate over each feature
            for feature in features:
                properties = feature['properties']
                geometry = feature['geometry']
                
                # Access specific properties and geometry
                name = properties['Name']
                coordinates = geometry['coordinates']
                
                print("Name:", name)
                print("Coordinates:", coordinates)
'''