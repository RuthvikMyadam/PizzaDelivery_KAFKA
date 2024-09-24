from faker import Faker
from pizzaproducer import PizzaProvider

fake = Faker()

fake.add_provider(PizzaProvider)
for i in range(0, 10):
    print(fake.pizza_name())