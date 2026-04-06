from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from dealerships.models import Dealer
from reviews.models import Review
from cars.models import CarMake, CarModel
from datetime import date

class Command(BaseCommand):
    help = 'Populate database with sample data for Cars Dealership'

    def handle(self, *args, **options):
        self.stdout.write('Populating database with sample data...')
        
        # Create sample users
        self.create_users()
        
        # Create sample dealers
        self.create_dealers()
        
        # Create sample car makes and models
        self.create_cars()
        
        # Create sample reviews
        self.create_reviews()
        
        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample data')
        )

    def create_users(self):
        """Create sample users"""
        users_data = [
            {
                'username': 'testuser',
                'first_name': 'Test',
                'last_name': 'User',
                'email': 'testuser@example.com',
                'password': 'testpass123'
            },
            {
                'username': 'john_doe',
                'first_name': 'John',
                'last_name': 'Doe',
                'email': 'john.doe@example.com',
                'password': 'password123'
            },
            {
                'username': 'sarah_smith',
                'first_name': 'Sarah',
                'last_name': 'Smith',
                'email': 'sarah.smith@example.com',
                'password': 'password123'
            }
        ]
        
        for user_data in users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'first_name': user_data['first_name'],
                    'last_name': user_data['last_name'],
                    'email': user_data['email']
                }
            )
            if created:
                user.set_password(user_data['password'])
                user.save()
                self.stdout.write(f'Created user: {user.username}')

    def create_dealers(self):
        """Create sample dealers"""
        dealers_data = [
            {
                'name': 'Premium Auto Kansas City',
                'city': 'Kansas City',
                'state': 'Kansas',
                'address': '1234 Auto Plaza Drive, Kansas City, KS 66101',
                'zip_code': '66101',
                'phone': '(913) 555-0123',
                'email': 'info@premiumautokc.com',
                'website': 'https://www.premiumautokc.com',
                'latitude': 39.114053,
                'longitude': -94.627464
            },
            {
                'name': 'Elite Motors Wichita',
                'city': 'Wichita',
                'state': 'Kansas',
                'address': '5678 Commerce Street, Wichita, KS 67202',
                'zip_code': '67202',
                'phone': '(316) 555-0456',
                'email': 'sales@elitemotorswichita.com',
                'website': 'https://www.elitemotorswichita.com',
                'latitude': 37.687176,
                'longitude': -97.330053
            },
            {
                'name': 'Metro Car Center Detroit',
                'city': 'Detroit',
                'state': 'Michigan',
                'address': '9876 Motor City Boulevard, Detroit, MI 48201',
                'zip_code': '48201',
                'phone': '(313) 555-0789',
                'email': 'contact@metrocardetroit.com',
                'website': 'https://www.metrocardetroit.com',
                'latitude': 42.331427,
                'longitude': -83.045754
            },
            {
                'name': 'Sunshine Auto Florida',
                'city': 'Miami',
                'state': 'Florida',
                'address': '2468 Ocean Drive, Miami, FL 33139',
                'zip_code': '33139',
                'phone': '(305) 555-0321',
                'email': 'info@sunshineautoflorida.com',
                'website': 'https://www.sunshineautoflorida.com',
                'latitude': 25.761680,
                'longitude': -80.191790
            }
        ]
        
        for dealer_data in dealers_data:
            dealer, created = Dealer.objects.get_or_create(
                name=dealer_data['name'],
                defaults=dealer_data
            )
            if created:
                self.stdout.write(f'Created dealer: {dealer.name}')

    def create_cars(self):
        """Create sample car makes and models"""
        car_data = [
            {
                'make': {
                    'name': 'Toyota',
                    'description': 'Japanese automotive manufacturer known for reliability and fuel efficiency',
                    'country': 'Japan',
                    'founded_year': 1937
                },
                'models': [
                    {'name': 'Camry', 'car_type': 'sedan', 'year': 2024, 'price_range': '$25,000 - $35,000', 'fuel_type': 'Gasoline/Hybrid'},
                    {'name': 'RAV4', 'car_type': 'suv', 'year': 2024, 'price_range': '$30,000 - $40,000', 'fuel_type': 'Gasoline/Hybrid'},
                    {'name': 'Prius', 'car_type': 'hatchback', 'year': 2024, 'price_range': '$28,000 - $35,000', 'fuel_type': 'Hybrid'}
                ]
            },
            {
                'make': {
                    'name': 'Honda',
                    'description': 'Japanese automotive manufacturer focusing on innovation and efficiency',
                    'country': 'Japan',
                    'founded_year': 1948
                },
                'models': [
                    {'name': 'Accord', 'car_type': 'sedan', 'year': 2024, 'price_range': '$26,000 - $38,000', 'fuel_type': 'Gasoline/Hybrid'},
                    {'name': 'CR-V', 'car_type': 'suv', 'year': 2024, 'price_range': '$28,000 - $36,000', 'fuel_type': 'Gasoline'},
                    {'name': 'Civic', 'car_type': 'sedan', 'year': 2024, 'price_range': '$23,000 - $30,000', 'fuel_type': 'Gasoline'}
                ]
            },
            {
                'make': {
                    'name': 'Ford',
                    'description': 'American automotive manufacturer with a rich heritage',
                    'country': 'United States',
                    'founded_year': 1903
                },
                'models': [
                    {'name': 'F-150', 'car_type': 'pickup', 'year': 2024, 'price_range': '$35,000 - $70,000', 'fuel_type': 'Gasoline/Electric'},
                    {'name': 'Mustang', 'car_type': 'coupe', 'year': 2024, 'price_range': '$32,000 - $60,000', 'fuel_type': 'Gasoline'},
                    {'name': 'Explorer', 'car_type': 'suv', 'year': 2024, 'price_range': '$36,000 - $55,000', 'fuel_type': 'Gasoline'}
                ]
            }
        ]
        
        for make_data in car_data:
            make, created = CarMake.objects.get_or_create(
                name=make_data['make']['name'],
                defaults=make_data['make']
            )
            if created:
                self.stdout.write(f'Created car make: {make.name}')
            
            for model_data in make_data['models']:
                model, created = CarModel.objects.get_or_create(
                    make=make,
                    name=model_data['name'],
                    year=model_data['year'],
                    defaults=model_data
                )
                if created:
                    self.stdout.write(f'Created car model: {make.name} {model.name}')

    def create_reviews(self):
        """Create sample reviews"""
        try:
            # Get sample data
            dealer1 = Dealer.objects.get(name='Premium Auto Kansas City')
            user1 = User.objects.get(username='john_doe')
            user2 = User.objects.get(username='sarah_smith')
            
            reviews_data = [
                {
                    'dealer': dealer1,
                    'user': user1,
                    'rating': 5,
                    'review_text': 'Fantastic services! The staff was incredibly helpful and professional. I found the perfect car at a great price. Highly recommend this dealership to anyone looking for quality vehicles and excellent customer service.',
                    'purchase_date': date(2024, 3, 15),
                    'car_make': 'Toyota',
                    'car_model': 'Camry',
                    'car_year': 2024,
                    'sentiment': 'positive'
                },
                {
                    'dealer': dealer1,
                    'user': user2,
                    'rating': 4,
                    'review_text': 'Good experience overall. The sales team was knowledgeable and the process was smooth. Minor wait time but worth it for the quality of service.',
                    'purchase_date': date(2024, 3, 20),
                    'car_make': 'Honda',
                    'car_model': 'Accord',
                    'car_year': 2023,
                    'sentiment': 'positive'
                }
            ]
            
            for review_data in reviews_data:
                review, created = Review.objects.get_or_create(
                    dealer=review_data['dealer'],
                    user=review_data['user'],
                    defaults=review_data
                )
                if created:
                    self.stdout.write(f'Created review by {review.user.username} for {review.dealer.name}')
                    
        except (Dealer.DoesNotExist, User.DoesNotExist) as e:
            self.stdout.write(f'Error creating reviews: {e}')