import factory

from django.contrib.auth.models import User

from order.models import Order

class UserFactory(factory.django.DajngoModelFactory):
    email = factory.Faker('pystr')
    username = factory.Faker('pystr')

    class Meta:
        model = User


class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    
    @factory.post_generation
    def produtc(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            for produtc in extracted:
                self.produtc.add(produtc)
    
    class Meta:
        model = Order