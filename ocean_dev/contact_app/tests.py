import json

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

User = get_user_model()


class TestSetup(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser('admin@gmail.com', 'Password@123')
        self.sme_user = User.objects.create_user(email="test@gmail.com", first_name="sss",
                                                 last_name="s",
                                                 phone_number=1233, user_role=2, credit_limit=243522,
                                                 currency_value="USD", is_user_onboard=True)


class TestLeadsModel(TestSetup):

    def test_create_contact(self):
        contact_url = "/contacts/contact/"
        contact_data = {
            "name": "Sajin",
            "mobile": "+91-00000",
            "email_address": "sajin@gmail.com",
            "message": "test contact message"
        }
        res = self.client.post(contact_url, contact_data)
        # pdb.set_trace()
        self.assertEquals(res.status_code, status.HTTP_201_CREATED)

    def test_list_contacts(self):
        self.client.force_authenticate(user=self.user)
        contact_url = "/contacts/contact/"
        self.test_create_contact()
        list_result = self.client.get(contact_url)
        # import pdb; pdb.set_trace()
        self.assertEqual(list_result.status_code, status.HTTP_200_OK)

    def test_create_leads_get_started_form(self):
        self.client.force_authenticate(user=None)
        lead_url = "/contacts/lead/"
        lead_data = {
            "first_name": "akshay.kr+1@seqato.com",
            "last_name": "akshay",
            "company_name": "akshay.kr+1@seqato.com",
            "company_email": "akshay.kr+1@seqato.com",
            "company_website": "https://thisisocean.com/",
            "phone_number": "+91-06",
            "company_registered_in": "US",
            "annual_revenue": "$500k - $1M",
            "description": "yes",
            "role": 2,
            "company_type": 3,
            "password": "Password@123"
        }
        response = self.client.post(lead_url, lead_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # import pdb;
        # pdb.set_trace()

        bytes_data = response.content
        user_details = json.loads(bytes_data.decode('utf-8'))
        return user_details

    def test_create_leads_admin(self):
        lead_url = "/contacts/lead/"
        lead_data = {
            "first_name": "akshay.kr+1@seqato.com",
            "last_name": "akshay",
            "company_name": "akshay.kr+1@seqato.com",
            "company_email": "akshay.kr+1@seqato.com",
            "company_website": "https://thisisocean.com/",
            "phone_number": "+91-06",
            "company_registered_in": "US",
            "annual_revenue": "$500k - $1M",
            "description": "yes",
            "role": 2
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(lead_url, lead_data, format='json')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        bytes_data = response.content
        user_details = json.loads(bytes_data.decode('utf-8'))
        return user_details

    def test_create_supplier_sme(self):
        lead_url = "/contacts/lead/"
        lead_data = {
            "first_name": "akshay.kr+1@seqato.com",
            "last_name": "akshay",
            "company_name": "akshay.kr+1@seqato.com",
            "company_email": "akshay.kr+1@seqato.com",
            "company_website": "https://thisisocean.com/",
            "phone_number": "+91-06",
            "company_registered_in": "US",
            "annual_revenue": "$500k - $1M",
            "description": "yes",
            "role": 3
        }
        self.client.force_authenticate(user=self.sme_user)
        response = self.client.post(lead_url, lead_data, format='json')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_email_already_exist(self):
        email_check_url = "/contacts/email/check/"
        self.test_create_leads_admin()
        email = {"company_email": "akshay.kr+1@seqato.com"}
        response = self.client.post(email_check_url, email, format='json')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_email_already_not_exist(self):
        email_check_url = "/contacts/email/check/"
        self.test_create_leads_admin()
        email = {"company_email": "abc@gmail.com"}
        response = self.client.post(email_check_url, email, format='json')
        # import pdb;
        # pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_phone_number_already_exist(self):
        email_check_url = "/contacts/phone_number/check/"
        self.test_create_leads_admin()
        email = {"phone_number": "+91-06"}
        response = self.client.post(email_check_url, email, format='json')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_phone_number_already_not_exist(self):
        email_check_url = "/contacts/phone_number/check/"
        self.test_create_leads_admin()
        email = {"phone_number": "89436596850"}
        response = self.client.post(email_check_url, email, format='json')
        # import pdb;
        # pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_null_email(self):
        email_check_url = "/contacts/email/check/"
        self.test_create_leads_admin()
        email = {"email": ""}
        response = self.client.post(email_check_url, email, format='json')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_null_phone_number(self):
        email_check_url = "/contacts/phone_number/check/"
        self.test_create_leads_admin()
        email = {"phone_number": ""}
        response = self.client.post(email_check_url, email, format='json')
        # import pdb;
        # pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_contries(self):
        country_url = "/contacts/countries/"
        response = self.client.get(country_url)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_currencies(self):
        currencies_url = "/contacts/currencies/"
        response = self.client.get(currencies_url)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_factor_user_creation(self):
        factor = "/contacts/lead/"
        self.client.force_authenticate(user=self.user)
        data = {
            "role": int(4),
            "company_email": "abc@gmail.com",
            "phone_number": "14522",
            "company_registered_in": "GB",
            "first_name": "Ninigolan"
        }
        response = self.client.post(factor, data, format='json')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
