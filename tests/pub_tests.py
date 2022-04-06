import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

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

    #@unittest.skip("Delete this line to run the test")
    def test_add_drink_to_stock(self):
        self.pub.add_drink_to_stock("Tennents")
        self.assertEqual(1, self.pub.drinks_list())
    
    #@unittest.skip("Delete this line to run the test")
    def test_remove_drink_from_stock(self):
        self.pub.add_drink_to_stock("Tennents")
        self.pub.remove_drink_from_stock("Tennents")
        self.assertEqual(0, self.pub.drinks_list())

    #@unittest.skip("Delete this line to run the test")
    def test_sell_drink_to_customer(self):
        customer = Customer("Susan", 50)
        drink = Drink("Tennents", 10)
        self.pub.add_drink_to_stock(drink)
        self.pub.sell_drink_to_customer(drink, customer)
        self.assertEqual(40, customer.wallet)
        self.assertEqual(1010, self.pub.till_value)
        self.assertEqual(0, self.pub.drinks_list())
        self.assertEqual(1, customer.customer_drinks())




    # def test_can_sell_pet_to_customer(self):
    #     customer = Customer("Jack Jarvis", 1000)
    #     self.pet_shop.sell_pet_to_customer("Sir Percy", customer)
    #     self.assertEqual(500, customer.cash)
    #     self.assertEqual(1500, self.pet_shop.total_cash)
    #     self.assertEqual(1, self.pet_shop.pets_sold)
    #     self.assertEqual(1, self.pet_shop.stock_count())
    #     self.assertEqual(1, customer.pet_count())



