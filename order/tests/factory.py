import factory

from django.contrib.auth.models import User
from product.tests.factory import ProductFactory

from order.models import Order

class UserFactory(factory.django.DajngoModelFactory):
    email = factory.Faker('pystr')
    username = factory.Faker('pystr')

    class Meta:
        model = User


class OrderFactory(factory.django.DajngoModelFactory):
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def produtc(self, create, extrated, **kwargs):
        if not create:
            return
        
        if extrated:
            for produtc in extrated:
                self.produtc.add(produtc)
    
    class Meta:
        model = Order