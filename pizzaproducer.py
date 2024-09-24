import random
from faker.providers import BaseProvider

class PizzaProvider(BaseProvider):
    def pizza_name(self):
        validPizzaNames = ['Pepperoni',
                            'Margherita',
                            'Hawaiian',
                            'ExtravaganZZa',
                            'MeatZZa',
                            'Veggie',
                            'Buffalo Chicken',
                            'BBQ Chicken',
                            'Spinach & Feta',
                            'Cheese'
                            ]
        return validPizzaNames[random.randint(0,len(validPizzaNames)-1)]