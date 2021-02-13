from django.test import TestCase

class SomeModelModelTest(TestCase):
    def setUp(self):
        SomeModel.objects.create(
            name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
            message=fake.message(),
            source=fake.url(),å
        )

    def test_save_model(self):
        saved_models = Somemodel.objects.count()
        self.assertEqual(saved_models, 2)