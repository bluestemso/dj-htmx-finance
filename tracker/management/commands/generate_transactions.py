import random
from faker import Faker
from django.core.management.base import BaseCommand
from tracker.models import User, Category, Transaction


class Command(BaseCommand):
    help = "Generate transactions for testing"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # create categories
        categories = [
            "Food",
            "Transport",
            "Entertainment",
            "Salary",
            "Medical",
            "Clothing",
            "Rent",
            "Utilities",
            "Other",
        ]

        for category in categories:
            Category.objects.get_or_create(name=category)

        # get the User
        user = User.objects.filter(username="bluestem").first()
        if not user:
            user = User.objects.create_superuser(
                username="bluestem", email="taylor@bluestem.solutions", password="test"
            )

        # generate 20 transactions
        categories = Category.objects.all()
        types = [x[0] for x in Transaction.TRANSACTION_TYPE_CHOICES]
        for i in range(20):
            Transaction.objects.create(
                category=random.choice(categories),
                user=user,
                amount=random.uniform(1, 2500),
                date=fake.date_between(start_date="-1yr", end_date="today"),
                type=random.choice(types),
            )
