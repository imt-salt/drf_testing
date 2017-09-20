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

    def test_options_returns_types_and_attributes(self):
        url = reverse('policy:policy')
        response = self.client.options(url, content_type='application/vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected = '''{
            "data": {
                "type": "Policy",
                "fields": {
                    "id": {
                        "label": "Id",
                        "read_only": true,
                        "allow_null": false,
                        "required": false
                    },
                    "policy_number": {
                        "max_length": 10,
                        "allow_null": false,
                        "required": true,
                        "label": "Policy number",
                        "allow_blank": false,
                        "read_only": false
                    }
                }
            }
        }'''
        self.assertEqual(response.json(), json.loads(expected))

    def test_x(self):
        data = {
            "data": {
                "type": "policy",
                "id": 1,
                "attributes": {
                    "policy_number": "123456"
                },
                "relationships": {
                    "coverages": {
                        "data": [
                            {
                                "type": "coverage",
                                "id": 23,
                            }
                        ]
                    }
                }
            },
            "included": [
                {
                    "type": "coverage",
                    "id": 23,
                    "attributes": {
                        "liability": False,
                        "coverage_type": "Awesome"
                    }
                }
            ]
        }
        url = reverse('policy:policy')
        response = self.client.post(url, data=json.dumps(data), content_type='application/vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.data)
        print(json.dumps(data))
        self.fail('x')
