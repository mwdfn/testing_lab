import unittest

#from src.pub import Pub
#from src.drink import Drink 
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Dave", 20)

    #@unittest.skip("Delete this line to run the test")

    def test_customer_has_name(self):
        self.assertEqual("Dave", self.customer.name)
