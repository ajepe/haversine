"""Implementation of Haversine formula 

    @link: https://en.wikipedia.org/wiki/Haversine_formula

    To determine the great-circle distance between two points on a sphere
    given their longitudes and latitudes where {R} is the radius of the 
    earth.
    
    e.g distance((6.6059619 [lat, 3.349483[lng),(7.6059619[lat, 4.444444[lng))
"""
import math


class Haversine(object):
    """This uses the ‘haversine’ formula to calculate the great-circle
    distance between two points – that is, the shortest distance over
    the earth’s surface.

    Giving an 'as-the-crow-flies' distance between the points 
    (ignoring any hills they fly over, of course!).
    """

    def __init__(self, radius=6371):
        """."""
        self.EARTH_RADIUS = radius

    @property
    def get_location_a(self) -> tuple:
        return self.LOCATION_ONE

    property

    def get_location_b(self) -> tuple:
        return self.LOCATION_TWO

    def distance(self, point_a: tuple, point_b: tuple) -> float:
        """Public api for haversine formula."""
        if not (isinstance(point_a, tuple) and isinstance(point_b, tuple)):
            raise TypeError(
                """Expect point_a and point_b to be <class "tuple">, {} and {} were given""".format(
                    type(point_a), type(point_b)
                )
            )
        self.LOCATION_ONE = point_b
        self.LOCATION_TWO = point_a
        return self._calculate_distance(self.LOCATION_ONE, self.LOCATION_TWO)

    def _calculate_distance(self, pointA, pointB):

        latA, lngA = (float(i) for i in pointA)
        latB, lngB = (float(i) for i in pointB)
        phiA = math.radians(latA)
        phiB = math.radians(latB)
        change_in_latitude = math.radians(latB - latA)
        change_in_longitude = math.radians(lngB - lngA)
        a = (
            math.sin(change_in_latitude / 2.0) ** 2
            + math.cos(phiA) * math.cos(phiB) * math.sin(change_in_longitude / 2.0) ** 2
        )
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = self.EARTH_RADIUS * c
        return distance
