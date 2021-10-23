from DAL.databaseDAL import DatabaseDAL


class Cashier:

    def __init__(self, order):
        """Initializes the cashier"""
        self.received_amount = 0
        self.order = order
        self.coins = self.__load_data('coins.json')

    def __load_data(self, file) -> list:
        """Simulates data loading for acceptable coins"""
        data = DatabaseDAL.load_data(file)
        return data["coins"]

    def check(self):
        """Verify the amount provided to pay the bill"""
        while self.received_amount < self.order["price"]:
            if self.received_amount == 0:
                message = f'Please insert coins to pay!\nAcceptable coins are: {self.coins} -> '
            else:
                message = f'Total inserted: {(self.received_amount/100):.2f}\nPlease insert coins to pay!\nAcceptable ' \
                          f'coins are: {self.coins} -> '

            amount = input(message)
            if amount in self.coins:
                amount = int(amount)
                self.received_amount += amount
            else:
                print('Invalid coin')

        print(f'Total amount inserted: {self.received_amount}\nProceeding to checkout...')
        change = self.provide_change(self.order["price"], self.received_amount)
        print('Thanks to buy at ACME Machines')
        print('Your change:')
        print(change)


    def provide_change(self, price, amount):
        """Calculates the change"""
        difference = amount - price
        change = {
            "200": 0,
            "100": 0,
            "25": 0,
            "10": 0,
            "5": 0
        }

        while not difference == 0:
            change["200"] = int(difference / 200)
            difference = difference % 200

            change["100"] = int(difference / 100)
            difference = difference % 100

            change["25"] = int(difference / 25)
            difference = difference % 25

            change["10"] = int(difference / 10)
            difference = difference % 10

            change["5"] = int(difference / 5)
            difference = difference % 5

        return change
