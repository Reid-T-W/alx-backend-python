#!/usr/bin/env python3
"""
Testing client.py
"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
requests = __import__("utils").requests
GithubOrgClient = __import__("client").GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Testing GithubOrgClient
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('requests.get')
    def test_org(self, org_name, mock_get_json):
        """
        Testing GithubOrgClient
        """
        instance = GithubOrgClient(org_name)
        # Mocking the response object
        mock_response = MagicMock()
        mock_response.json.return_value = {"payload": True}

        # Assigning the mocked response object to the mocked
        # request.get object
        mock_get_json.return_value = mock_response

        doc = instance.org
        doc = instance.org

        # Since the org method is decorated by @memoize
        # the get_json function should only be executed once,
        # hence the mocked get function is executed only once
        mock_get_json.assert_called_once()
        self.assertEqual(doc, {"payload": True})
