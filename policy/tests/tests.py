import simplejson as json

from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse


class SerializerTest(TestCase):

    def test_data_validates(self):
        data = {
            "data": {
                "type": "policy",
                "id": 1,
                "attributes": {
                    "policy_number": "123abc"
                }
            }
        }
        url = reverse('policy:policy')
        response = self.client.post(url, data=json.dumps(data), content_type='application/vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected = json.loads('{"data":{"type":"policy","id":null,"attributes":{"policy_number":"123abc"}}}')
        self.assertEqual(expected, response.json())

    def test_receives_validation_errors(self):
        data = {
            "data": {
                "type": "policy",
                "id": 1,
                "attributes": {
                    "policy_number": "1234567890abc"
                }
            }
        }
        url = reverse('policy:policy')
        response = self.client.post(url, data=json.dumps(data), content_type='application/vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected = {'policy_number': ['Ensure this field has no more than 10 characters.']}
        response_json = response.json()
        self.assertTrue(response_json['data']['error'])
        self.assertEqual(response_json['data']['errors'], expected)
