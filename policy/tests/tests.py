import simplejson as json

from django.test import TestCase
from rest_framework.reverse import reverse


class SerializerTest(TestCase):

    def test_x(self):
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
        print(response)
        print(response.content)
        self.fail('x')
