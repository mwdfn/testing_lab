import unittest

from src.pub import Pub
#from src.drink import Drink 
#from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Black Bull", 1000)

    #@unittest.skip("Delete this line to run the test")
    def test_pub_has_name(self):
        self.assertEqual("Black Bull", self.pub.name)

    #@unittest.skip("Delete this line to run the test")
    def test_till_value_total(self):
        self.assertEqual(1000, self.pub.till_value)

    #@unittest.skip("Delete this line to run the test")
    def test_return_list_of_drinks(self):
        self.assertEqual(0, self.pub.drinks_list())

    #@unittest.skip("Delete this line to run the test")
    def test_increase_till_total(self):
        self.pub.add_money_to_till(5)
        self.assertEqual(1005, self.pub.till_value)



