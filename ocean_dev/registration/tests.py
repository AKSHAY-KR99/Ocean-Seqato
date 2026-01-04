import json

from django.contrib.auth import get_user_model
from rest_framework import status
from contact_app.tests import TestLeadsModel

User = get_user_model()


class TestRegistrationAPIs(TestLeadsModel):

    def test_list_user(self):
        self.client.force_authenticate(user=self.user)
        is_active = 0
        user_role = 2
        list_url = f"/account/user/?is_active={is_active}&user_role={user_role}"
        self.test_create_leads_admin()
        response = self.client.get(list_url)
        # import pdb;
        # pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_admin(self):
        self.client.force_authenticate(user=self.user)

        update_data = {
            "user_active_status": True,
            "credit_limit": 9877,
            "first_name": "Siddique",
            "last_name": "Saddique",
            "country_name": "US"
        }
        user = self.test_create_leads_admin()
        url = f"/account/user/{user['sme_id']}/"
        response = self.client.put(url, update_data, format='json')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_by_user(self):
        new_user = User.objects.create_user(email="kingdavid@ing.com", first_name="sss",
                                            last_name="s",
                                            phone_number=7896541230, user_role=2, credit_limit=243522,
                                            currency_value="USD", is_user_onboard=True, is_active=True)
        url = f"/account/user/{new_user.id}/"
        self.client.force_authenticate(user=new_user)
        update_data = {
            "first_name": "Siddique",
            "last_name": "Saddique",
            "phone_number": "2255"
        }
        response = self.client.put(url, update_data, format='json')
        # import pdb;
        # pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_password_set_admin_created_user(self):
        password_url = "/account/password/set/"
        user = self.test_create_leads_admin()
        request_data = {
            'email': user['sign_up_email'],
            'password': 'Password@123'
        }
        response = self.client.post(password_url, request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # import pdb;pdb.set_trace()
        bytes_data = response.content
        return json.loads(bytes_data.decode('utf-8'))

    def test_otp_validation_admin_created_user(self):
        user = self.test_password_set_admin_created_user()
        otp_validate_url = "/account/otp/validate/"
        request_data = {
            "session_id": user['session_id'],
            "otp_value": 777777
        }
        response = self.client.post(otp_validate_url, request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # import pdb; pdb.set_trace()
        return user['session_id']

    def test_auth_token_generate(self):
        token_url = "/account/token/generate/"
        session = self.test_otp_validation_admin_created_user()
        request_data = {
            "session_id": session,
            "password": "Password@123"
        }
        response = self.client.post(token_url, request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # import pdb;
        # pdb.set_trace()

    def test_otp_validation_get_started_user(self):
        user = self.test_create_leads_get_started_form()
        otp_validate_url = "/account/otp/validate/"
        request_data = {
            "session_id": user['session_id'],
            "otp_value": 777777
        }
        response = self.client.post(otp_validate_url, request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # import pdb; pdb.set_trace()
        return user['session_id']

    def test_auth_token_generate_get_started_user(self):
        token_url = "/account/token/generate/"
        session = self.test_otp_validation_get_started_user()
        request_data = {
            "session_id": session,
            "password": "Password@123"
        }
        response = self.client.post(token_url, request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # import pdb;
        # pdb.set_trace()
