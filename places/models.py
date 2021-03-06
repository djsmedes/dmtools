from typing import Type
from shapely.wkb import loads as wkb_loads
from shapely.geometry.base import BaseGeometry
from shapely.geometry import Point, LineString, Polygon
from django.db import models

from base.models import BaseModel


class Place(BaseModel):
    # lore-related details

    description = models.TextField(null=True, blank=True)

    MISC_REGION = 200
    GEOLOGICAL = 201
    VEGETATION = 202
    WATER = 203
    POLITICAL = 204

    MISC_LINE = 100
    ROAD = 101
    RIVER = 102

    MISC_POINT = 0
    SETTLEMENT = 1
    NATURAL = 2
    DUNGEON = 3

    TYPE_CHOICES = [
        (MISC_REGION, 'misc region'),
        (GEOLOGICAL, 'geological'),
        (VEGETATION, 'vegetation'),
        (WATER, 'water'),
        (POLITICAL, 'political'),

        (MISC_LINE, 'misc line'),
        (ROAD, 'road'),
        (RIVER, 'river'),

        (MISC_POINT, 'misc point'),
        (SETTLEMENT, 'settlement'),
        (NATURAL, 'natural'),
        (DUNGEON, 'dungeon'),
    ]

    type = models.IntegerField(choices=TYPE_CHOICES, null=True, blank=True)

    # location-related details

    POINT = 0
    LINE = 1
    POLYGON = 2
    DIMENSIONS_CHOICES = [
        (POINT, 'point'),
        (LINE, 'line'),
        (POLYGON, 'polygon')
    ]

    _shape = models.BinaryField(db_column='shape', null=True, blank=True)
    _dimensions = models.IntegerField(db_column='dimensions', choices=DIMENSIONS_CHOICES, null=True, blank=True)
    _shapely_object = None
    other_places = models.ManyToManyField(
        'self', through='places.PlacePair',
        through_fields=('place1', 'place2'),
        symmetrical=False,
    )

    @property
    def shape(self):
        if self._shape is None:
            return None
        if self._shapely_object is None:
            self._shapely_object = wkb_loads(bytes(self._shape))
        return self._shapely_object

    @shape.setter
    def shape(self, shape: Type[BaseGeometry]):
        self._shapely_object = shape
        if shape is None:
            self._shape = None
        else:
            self._shape = shape.wkb
        self._dimensions = self.dimensions

    @property
    def dimensions(self):
        if isinstance(self.shape, Point):
            return self.POINT  # 0
        elif isinstance(self.shape, LineString):
            return self.LINE  # 1
        elif isinstance(self.shape, Polygon):
            return self.POLYGON  # 2
        else:
            return None

    @property
    def points(self):
        if self.type < 200:
            # points or lines use attr .coords directly
            pts = list(self.shape.coords)
        else:
            # it's a polygon, which you have to get the exterior attr of first
            # and also it lists start and end point as the same point, so slice that sucker off
            pts = self.shape.exterior.coords[:-1]
        return [{'x': int(pt[0]), 'y': int(pt[1])} for pt in pts]

    @points.setter
    def points(self, points: dict):
        if not self.type and self.type != 0:
            raise ValueError('Cannot set points on object until "type" attribute has been set.')
        coords = [(pt['x'], pt['y']) for pt in points]
        if self.type < 100:
            self.shape = Point(coords)
        elif self.type < 200:
            self.shape = LineString(coords)
        else:
            self.shape = Polygon(coords)

    def __str__(self):
        return self.name

    def get_nearby_places(self, within_distance=0):
        ret = []
        for placepair in self.placepairs_out.all():
            if placepair.min_distance <= within_distance:
                ret.append(placepair.place2)
            else:
                break
        return ret


class PlacePair(models.Model):
    place1 = models.ForeignKey('places.Place', on_delete=models.CASCADE, related_name='placepairs_out')
    place2 = models.ForeignKey('places.Place', on_delete=models.CASCADE, related_name='placepairs_in')
    min_distance = models.FloatField()

    class Meta:
        ordering = ['min_distance']

    def __str__(self):
        return '{} -> {}'.format(self.place1.name, self.place2.name)
