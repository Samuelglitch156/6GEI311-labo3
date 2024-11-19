# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.cours import Cours  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCoursController(BaseTestCase):
    """CoursController integration test stubs"""

    def test_cours_get(self):
        """Test case for cours_get

        Obtenir la liste des cours
        """
        response = self.client.open(
            '/cours',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cours_id_delete(self):
        """Test case for cours_id_delete

        Supprimer un cours
        """
        response = self.client.open(
            '/cours/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cours_id_get(self):
        """Test case for cours_id_get

        Obtenir un cours par son identifiant
        """
        response = self.client.open(
            '/cours/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cours_id_put(self):
        """Test case for cours_id_put

        Mettre à jour un cours existant
        """
        body = Cours()
        response = self.client.open(
            '/cours/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cours_post(self):
        """Test case for cours_post

        Ajouter un nouveau cours
        """
        body = Cours()
        response = self.client.open(
            '/cours',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
