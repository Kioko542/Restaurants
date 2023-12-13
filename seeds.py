from models import Restaurant, Customer, Review, session

# Create sample data
restaurant1 = Restaurant(name='Restaurant A', price=3)
restaurant2 = Restaurant(name='Restaurant B', price=4)
customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Smith')

review1 = Review(star_rating=5, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=4, restaurant=restaurant2, customer=customer1)
review3 = Review(star_rating=3, restaurant=restaurant1, customer=customer2)

session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2, review3])
session.commit()
