import unittest
from app import Cart,Customers,Customer
from test_data import TestData

CUSTOMERS_DATA = [['Arun',1,1,datetime.datetime(2018,4,20)],
                  ['John',0,1,datetime.datetime(2015,5,21)],
                  ['Atul',1,0,datetime.datetime(2011,7,26)],
                  ['Ram',0,0,datetime.datetime(2015,4,20)]]

class TestCartDiscounts(unittest.TestCase):
    def test_chai_apples(self):
        cust = customers.get_customer_by_customer_name('Arun')
        customer = Customer(cust.name,cust.eid,cust.aid,cust.joinDate)
        test_chai_apples_cart = Cart(customer)
        test_chai_apples_cart.add_multiple_products_to_cart(['CH1', 'AP1'])
        total = test_chai_apples_cart.display()[1]
        self.assertEqual(total, 9.11)



if __name__ == '__main__':
    unittest.main()
