from django.core.management.base import BaseCommand
from django_seed import Seed
from listings.models import Listing, Booking, Review
from django.contrib.auth import get_user_model
from random import randint, choice
from decimal import Decimal
from datetime import timedelta, date

User = get_user_model()

class Command(BaseCommand):
    help = "Seed the database with sample listings, users, bookings, and reviews"

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=5, help='Number of users to create')
        parser.add_argument('--listings', type=int, default=10, help='Number of listings to create')
        parser.add_argument('--bookings', type=int, default=20, help='Number of bookings to create')
        parser.add_argument('--reviews', type=int, default=15, help='Number of reviews to create')

    def handle(self, *args, **options):
        seeder = Seed.seeder()

        num_users = options['users']
        num_listings = options['listings']
        num_bookings = options['bookings']
        num_reviews = options['reviews']

        self.stdout.write(self.style.WARNING("Starting database seeding..."))

        seeder.add_entity(User, num_users, {
            'email': lambda x: seeder.faker.unique.email(),
            'first_name': lambda x: seeder.faker.first_name(),
            'last_name': lambda x: seeder.faker.last_name(),
            'role': 'user', 
        })

        seeder.add_entity(Listing, num_listings, {
            'owner': lambda x: choice(User.objects.all()),
            'name': lambda x: seeder.faker.street_name(),
            'description': lambda x: seeder.faker.text(max_nb_chars=200),
            'location': lambda x: seeder.faker.city(),
            'price_per_night': lambda x: Decimal(randint(50, 500)),
            'is_available': lambda x: choice([True, False]),
        })

        seeder.add_entity(Booking, num_bookings, {
            'listing': lambda x: choice(Listing.objects.all()),
            'guest': lambda x: choice(User.objects.all()),
            'start_date': lambda x: date.today(),
            'end_date': lambda x: date.today() + timedelta(days=randint(1, 7)),
            'number_of_guests': lambda x: randint(1, 5),
            'total_price': lambda x: Decimal(randint(200, 2000)),
            'status': lambda x: choice(['PENDING', 'CONFIRMED', 'CANCELLED']),
        })

        seeder.add_entity(Review, num_reviews, {
            'listing': lambda x: choice(Listing.objects.all()),
            'author': lambda x: choice(User.objects.all()),
            'rating': lambda x: randint(1, 5),
            'comment': lambda x: seeder.faker.text(max_nb_chars=150),
        })

        inserted_pks = seeder.execute()


        self.stdout.write(self.style.SUCCESS("✅ Database seeding completed successfully!"))
        self.stdout.write(self.style.SUCCESS(f"Created: {num_users} users, {num_listings} listings, {num_bookings} bookings, {num_reviews} reviews."))
