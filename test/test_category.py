# coding: utf-8

"""
    Swagger Petstore

    This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters.

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.category import Category


class TestCategory(unittest.TestCase):
    """ Category unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCategory(self):
        """
        Test Category
        """
        model = swagger_client.models.category.Category()


if __name__ == '__main__':
    unittest.main()
