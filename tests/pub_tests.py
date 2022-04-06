import unittest

from src.pub import Pub
from src.drink import Drink 
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Black Bull", 1000)

    @unittest.skip("Delete this line to run the test")
    def test_has_route_number(self):
        self.assertEqual(22, self.bus.route_number)


