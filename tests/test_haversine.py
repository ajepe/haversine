import unittest

from haversine import haversine


class TestHaversine(unittest.TestCase):
    """Test Haversine class"""

    def setUp(self):
    	self.haversine = haversine.Haversine()

    def test_diff_distance_calculation(self):
        """test great circle distance between location_a and location_b."""
        location_a = (45.7597, 4.8422)
        location_b = (48.8567, 2.3508)
        distance = self.haversine.distance(location_a, location_b)
        self.assertEqual(distance, 392.2167178065958)

    def test_same_distance_calculation(self):
        """test  distance between the same location."""
        location_a = (45.7597, 4.8422)
        location_b = (45.7597, 4.8422)
        distance = self.haversine.distance(location_a, location_b)
        message = 'Expect the distance between {} and {} to be 0.0'.format(location_a, location_b)
        self.assertEqual(distance, 0.0, msg=message)
