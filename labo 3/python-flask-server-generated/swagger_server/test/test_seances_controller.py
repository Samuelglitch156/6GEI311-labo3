# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.seance import Seance  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSeancesController(BaseTestCase):
    """SeancesController integration test stubs"""

    def test_cours_id_seances_get(self):
        """Test case for cours_id_seances_get

        Obtenir la liste des séances d'un cours
        """
        response = self.client.open(
            '/cours/{id}/seances'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
