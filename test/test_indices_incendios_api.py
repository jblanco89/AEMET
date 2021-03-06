# coding: utf-8

"""
    AEMET OpenData

    AEMET OpenData es una API REST desarrollado por AEMET que permite la difusión y la reutilización de la información meteorológica y climatológica de la Agencia, en el sentido indicado en la Ley 18/2015, de 9 de julio, por la que se modifica la Ley 37/2007, de 16 de noviembre, sobre reutilización de la información del sector público. (IMPORTANTE: Para poder realizar peticiones, es necesario introducir en API Key haciendo clic en el círculo rojo de recurso REST).  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.indices_incendios_api import IndicesIncendiosApi  # noqa: E501
from swagger_client.rest import ApiException


class TestIndicesIncendiosApi(unittest.TestCase):
    """IndicesIncendiosApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.indices_incendios_api.IndicesIncendiosApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_mapa_de_niveles_de_riesgo_estimado_meteorolgico_de_incendios_forestales_(self):
        """Test case for mapa_de_niveles_de_riesgo_estimado_meteorolgico_de_incendios_forestales_

        Mapa de niveles de riesgo estimado meteorológico de incendios forestales.  # noqa: E501
        """
        pass

    def test_mapa_de_niveles_de_riesgo_previsto_meteorolgico_de_incendios_forestales_(self):
        """Test case for mapa_de_niveles_de_riesgo_previsto_meteorolgico_de_incendios_forestales_

        Mapa de niveles de riesgo previsto meteorológico de incendios forestales.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
