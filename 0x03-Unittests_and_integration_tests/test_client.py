#!/usr/bin/env python3
"""
Testing client.py
"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
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

    def test_public_repos_url(self):
        """
        Test GithubOrgClient._public_repos_url
        """
        instance = GithubOrgClient('google')
        # Mocking the org method of GithubOrgClient, it is
        # considered a propoerty because the @memoize decorator
        # turns it into a property
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as org_mock:
            org_mock.return_value = {"repos_url": True}

            # The _public_repos_url method returns the value
            # associated with the key "repos_url"
            value = instance._public_repos_url
            self.assertEqual(value, True)
