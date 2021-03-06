from abstract_state import AbstractState

class NotEmpty(AbstractState):

    def add_item(self):
        self._cart.items += 1
        print('You now have %s items in your cart.' % self._cart.items)

    def remove_item(self):
        self._cart.items -= 1
        if self._cart.items:
            print('You now have %s items in your cart.' % self._cart.items)
        else:
            print('Your cart is empty again.')
            self._cart.state = self._cart.empty

    def checkout(self):
        print("Done shopping. Let's check out!")
        self._cart.state = self._cart.check_out

    def pay(self):
        print("You have to go to checkout to pay!")

    def empty_cart(self):
        print("Your can only empty the cart at checkout.")
