from BLL.machine import Machine
from BLL.cashier import Cashier


def start():
    """Starts the program to sell products"""
    machine = Machine('products.json')
    machine.show_menu()
    order = machine.ask_order()
    cashier = Cashier(order)
    cashier.check()


if __name__ == '__main__':
    start()