'''import json
from django.core.management.base import BaseCommand
from masark.models import Station'''

# yourapp/management/commands/import_roads.py

from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from masark.models import Road, Point  # Import your Road and Point models

class Command(BaseCommand):
    help = 'Import roads data'

    def handle(self, *args, **options):
        road_data = [...]  # Your road data
        for road_data in road_data:
            road = Road.objects.create(name=road_data['properties']['Name'],
                                       time=road_data['properties']['Time'],
                                       distance=road_data['properties']['Distance'])

            for coord in road_data['geometry']['coordinates']:
                point = Point.objects.create(road=road,
                                             latitude=coord[1],
                                             longitude=coord[0])


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