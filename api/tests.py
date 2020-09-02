from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.utils import json


class APIEndpointGetAllAthletes(APITestCase):
    def testResponseCodeSuccess(self):
        """
        """

        url = reverse("athletes")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testResponseType(self):
        """
        """

        url = reverse("athletes")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response._content_type_for_repr.split('"')[1], 'application/json')

    def testResponseStructure(self):
        """
        """

        url = reverse("athletes")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "athlete")
        contents = json.loads(response.content)
        self.assertEqual(len(contents["athlete"]), 8)

    def testResponseStructure2(self):
        """
        """

        url = reverse("athletes")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "athlete")
        nested_contents = (json.loads(response.content))["athlete"]
        self.assertEqual(len(nested_contents["1"]), 4)


class APIEndpointGetAthleteByID(APITestCase):
    def testResponseCodeSingleIDSuccess(self):
        """
        """

        url = reverse("athletes")
        data = {'id': '1'}
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testResponseCodeMultipleIDSuccess(self):
        """
        """

        url = reverse("athletes")
        data = {'id': ['1', '2']}
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testResponseCodeBadRequest(self):
        """
        """

        url = reverse("athletes")
        data = {'id': '99'}
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testResponseCodeBadParameter(self):
        """
        """

        url = reverse("athletes")
        data = {'number': "2"}
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testResponseCodeMixedIDsSuccess(self):
        """
        """

        url = reverse("athletes")
        data = {'id': ['1', '200']}
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testResponseAttributes(self):
        """
        """

        url = reverse("athletes")
        data = {'id': '2'}
        response = self.client.get(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertContains(response, "athlete")
        nested_contents = (json.loads(response.content))["athlete"]
        athlete = nested_contents["2"]
        self.assertEqual(athlete['firstName'], 'Nick')
        self.assertEqual(athlete['lastName'], 'Chubb')
        self.assertEqual(athlete['weight'], 70)
        self.assertEqual(athlete['height'], 1.69)


class BadPaths(APITestCase):
    def testBadPath(self):
        """
        """

        url = "/athlete/bad"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def testPOST(self):
        """
        """

        url = reverse("athletes")
        data = {"id": "3"}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def testDELETE(self):
        """
        """

        url = reverse("athletes")
        data = {"id": "3"}
        response = self.client.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def testPUT(self):
        """
        """

        url = reverse("athletes")
        data = {"id": "3"}
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class APIListViewGet(APITestCase):
    def testGetAll(self):
        """
        """
        url = reverse("listview")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testGetById(self):
        """
        """
        url = reverse("listview")
        data = {"id": "2"}

        response = self.client.get(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertContains(response, "athlete")
        nested_contents = (json.loads(response.content))["athlete"]
        athlete = nested_contents["2"]
        self.assertEqual(athlete['firstName'], 'Nick')
        self.assertEqual(athlete['lastName'], 'Chubb')
        self.assertEqual(athlete['weight'], 70)
        self.assertEqual(athlete['height'], 1.69)


class WebPage(APITestCase):
    def testStatusCode(self):
        """
        """
        url = reverse("webpage")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testTemplateUsed(self):
        """
        """
        url = reverse("webpage")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, "index.html")

    def testContents(self):
        """
        """
        url = reverse("webpage")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'searchDiv')

    def testScriptFile(self):
        """
        """
        url = reverse("webpage")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'app.js')
