from DAL.databaseDAL import DatabaseDAL


class Machine:

    def __init__(self, product_list):
        """Initializes the machine"""
        self.products = self.__load_data(product_list)
        self.options = []

    def __load_data(self, product_list):
        """Simulates data loading for product list"""
        data = DatabaseDAL.load_data(product_list)
        return data["products"]

    def show_menu(self):
        """Shows products menu"""
        print('See our offers menu:')
        for product in self.products:
            option = list(product.keys())[0]
            self.options.append(option)
            print(f'{option.rjust(2)} - {product[option]["name"].ljust(10)} - CAD {(product[option]["price"]/100):.2f}')

    def ask_order(self):
        """Talk to customer and wait for an option"""
        option = None
        while not option:
            option = input('Select an option to buy -> ')
            if option not in self.options:
                option = None
                print('Invalid option. Select by option number')

        print('great choice!')
        order = [p for p in self.products if list(p.keys())[0] == option][0][option]
        print(f'{order["name"]} - CAD {(order["price"]/100):.2f}')
        return order

