from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class RegisterViewTests(TestCase):
    def test_register_creates_user_and_logs_them_in(self):
        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "newuser",
                "email": "newuser@example.com",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/")

        user = get_user_model().objects.get(username="newuser")
        self.assertEqual(user.email, "newuser@example.com")
        self.assertIn("_auth_user_id", self.client.session)
        self.assertEqual(self.client.session["_auth_user_id"], str(user.pk))
