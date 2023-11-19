import factory

from product.models import Product
from product.models import Category

class CategoryFactory(factory.django.DajngoModelFactory):
    title = factory.Faker('pystr')
    slug = factory.Faker('pystr')
    description = factory.fake('pystr')
    active = factory.iterator([True, False])

    class Meta:
        model = Category

class ProductFactory(factory.django.DajngoModelFactory):
    price = factory.Faker('pyint')
    category = factory.LazyAttribute(CategoryFactory)
    title = factory.Faker('pyint')

    @factory.post_generation
    def category(self, create, extrated, **kwargs):
        if not create:
            return
        
        if extrated:
            for category in extrated:
                self.category.add(category)
    
    class Meta:
        model = Product