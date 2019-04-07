import copy
import datetime
# all grocery items has 1 at the end of code
PRODUCTS_DATA = [['CH1', 'Chai', 3.11],
                 ['AP1', 'Apples', 6.00],
                 ['CF1', 'Coffee', 11.23],
                 ['MK1', 'Milk', 4.75],
                 ['OM1', 'Oatmeal', 3.69],
                 ['EM5','Speakers',100],
                 ['EL2','Headphone',200],
                 ['MT3','Vaccum Cleaner' ,500]]
                 

# customer array [id , name , emp id  , affliate id  , joinDate ] 
CUSTOMERS_DATA = [['Arun',1,1,datetime.datetime(2018,4,20)],
                  ['John',0,1,datetime.datetime(2015,5,21)],
                  ['Atul',1,0,datetime.datetime(2011,7,26)],
                  ['Ram',0,0,datetime.datetime(2015,4,20)]]




class Products:
    def __init__(self):
        self.products = {}
        self.init_products()

    def add_product(self, product_code, name, price):
        self.products[product_code] = Product(product_code, name, price)

    def get_product_by_product_code(self, product_code):
        product_code = product_code.upper()
        return self.products[product_code] if product_code in self.products else None

    def init_products(self):
        for product in PRODUCTS_DATA:
            self.add_product(*product)


class Product:
    def __init__(self, product_code, name, price):
        self.product_code = product_code
        self.name = name
        self.price = price


class Customers:
    def __init__(self):
        self.customers = {}
        self.init_customers()

    def add_customer(self, name, eid , aid , joinDate):
        self.customers[name] = Customer(name , eid ,aid , joinDate)

    def get_customer_by_customer_name(self, name):
        name = name.capitalize()
        return self.customers[name] if name in self.customers else None

    def init_customers(self):
        for customer in CUSTOMERS_DATA:
            self.add_customer(*customer)


class Customer:
    def __init__(self, name, eid , aid ,joinDate ):
        self.name = name
        self.eid = eid
        self.aid = aid
        self.joinDate = joinDate 
        

class CartItem:
    def __init__(self, product_code, name, price):
        self.product_code = product_code
        self.name = name
        self.price = price


class Cart:
    def __init__(self,customer):
        
        self.customer = customer
        self.cart = []
        self.total_item_qty = {}

        self.percentDiscount = 0


    def add_item(self, cart_item):
        self.cart.append(copy.deepcopy(cart_item))
        if cart_item.product_code in self.total_item_qty:
            self.total_item_qty[cart_item.product_code] += 1
        else:
            self.total_item_qty[cart_item.product_code] = 1
            
    def cal_percentDiscount(self):
        if self.customer.eid:
            return 30
        elif self.customer.aid:
            return 10
        else:
            ddiff = datetime.datetime.now() - self.customer.joinDate
            difference_in_years = (ddiff.days + ddiff.seconds/86400)/365.2425
            if difference_in_years > 2:
                return 5
            
        
 
    def display(self):
       # self.calculate_discounts()
        # Display header
        percentDiscount = self.cal_percentDiscount()
        cart_display = ('{:<18}{:>17}\n{:<18}{:>17}\n'.format('Item', 'Price', '----', '-----'))
        cart_total = 0.0
        grocery_total  = 0.0
        nongrocery_total = 0.0
        
        if not self.cart:
            cart_display += '{:*^35}\n'.format(' EMPTY CART ')
        for cart_item in self.cart:
            # Display cart item
            cart_display += ('{:<18}{:17.2f}\n'.format(cart_item.product_code, cart_item.price))
            cart_total += cart_item.price
            if  cart_item.product_code[2] == '1':
                grocery_total += cart_item.price
            else:
                nongrocery_total += cart_item.price
        cart_total = round(cart_total, 2)
        nongrocery_total = round(nongrocery_total , 2)
        grocery_total = round(grocery_total , 2)
        cart_display += ('{:->36}{:>35.2f}\n\n'.format('\n', cart_total))
        nongrocery_net=nongrocery_total-(nongrocery_total*percentDiscount/100)
        gross_discount=(cart_total/100)*5
        net_total=nongrocery_net+grocery_total-gross_discount
        return cart_display,cart_total , nongrocery_total , grocery_total,percentDiscount,nongrocery_net,gross_discount,round(net_total,2)
                 
    def add_to_cart(self, product_code):
        item = products.get_product_by_product_code(product_code)
        if item is not None:
            self.add_item(CartItem(item.product_code, item.name, item.price))

    def add_multiple_products_to_cart(self, product_codes):
        for product_code in product_codes:
            self.add_to_cart(product_code)


class App:
    def __init__(self,customer):
        
        self.cart = Cart(customer)
        self.menu_items = ['1. Add to Cart',
                           '2. Display Cart',
                           '3. Exit']
        self.menu_options = {1: self.add_to_cart,
                             2: self.display_cart,
                             3: self.exit_app}
        self.menu_loop()

    def menu_input(self):
        # Display menu items and input selection
        print([ m for m in self.menu_items])
        return raw_input('Please select a menu item: ')

    def menu_loop(self):
        while True:
            # Loop until user exits
            menu_item = self.menu_input()
            # Get menu item number or loop back around
            try:
                menu_item = int(menu_item)
            except ValueError:
                pass
            # Exit
            if menu_item == len(self.menu_items):
                break
            # Valid menu item
            if menu_item in range(1, len(self.menu_items)):
                self.menu_options[menu_item]()

    def display_products(self):
        # Display available products
        border = '+{:-^14}|{:-^14}|{:-^9}+'.format('', '', '')
        header = '|{: ^14}|{: ^14}|{: ^9}|'.format('Product Code', 'Name', 'Price')
        print('{}\n{}\n{}'.format(border, header, border))
        print(['|{: ^14}|   {: <11}|{: >7}  |'.format(*product) for product in PRODUCTS_DATA])
        print(border+'\n')

        

    def add_to_cart(self):
        self.display_products()
        # Input product code(s)
        print('Enter one or more product codes (comma separated)')
        product_codes = raw_input('Product code(s): ')
        # Add product(s) to cart
        self.cart.add_multiple_products_to_cart([product_code.strip() for product_code in product_codes.split(',')])

    def display_cart(self):
        print(self.cart.customer.name)
        print(self.cart.display()[0])
        discount_percent=self.cart.display()[4]
        nongrocery_total=self.cart.display()[2]
        grocery_total= self.cart.display()[3]
        nongrocery_net = self.cart.display()[5]
        gross_discount= self.cart.display()[6]
        net_total = self.cart.display()[7]
        print('\nPercent Discount :' + str(discount_percent) + '% on Non-grocery items total: '+ str(nongrocery_total)+' gives: '+str(nongrocery_net));
        print('\nGross Discount 5$ for 100$ on bill : '+str(gross_discount))
        print('\nNetpayable amount : ' + str(net_total))
        
    def exit_app(self): return None


products = Products()
customers = Customers()

print[i[0] for i in CUSTOMERS_DATA] 
while True:
    cname = raw_input('Please select the customer name:')
    cust = customers.get_customer_by_customer_name(cname)
    if cust  : break 

customer = Customer(cust.name,cust.eid,cust.aid,cust.joinDate)
    
trans = App(customer);

