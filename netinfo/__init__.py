#!/usr/bin/env python
"""Abstract API over the Netinfo API."""
import json
import logging
import requests


__author__ = "Brandon Dixon"
__copyright__ = "Copyright, Netinfo"
__credits__ = ["Brandon Dixon"]
__license__ = "MIT"
__maintainer__ = "Brandon Dixon"
__email__ = "brandon@backscatter.io"
__status__ = "BETA"


class RequestFailure(Exception):
    """Exception to capture a failed request."""
    pass


class InvalidResponse(Exception):
    """Exception to capture a failed response parse."""
    pass


class Netinfo:

    """Abstract interface for Netinfo."""

    NAME = "Netinfo"

    def __init__(self, url):
        """Init the object."""
        self.url = url
        self.type_map = {
            'ip': 'lookup',
            'network': 'network-addresses',
            'as': 'as',
            'port': 'port',
            'asn': 'as'
        }

    def _request(self, endpoint, params=dict(), data=None):
        """Handle the requesting of information from the API."""
        client_value = "Python Netinfo"
        headers = {'X-Request-Client': client_value}
        url = '/'.join([self.url, endpoint])
        kwargs = {'url': url, 'headers': headers, 'timeout': 30,
                  'params': params, 'data': data}
        response = requests.get(**kwargs)
        if response.status_code not in range(200, 299):
            raise RequestFailure(response.status_code, response.content)
        try:
            loaded = json.loads(response.content)
        except Exception as error:
            raise InvalidResponse(error)
        return loaded

    def enrich(self, query, query_type):
        """Enrich data based on the type."""
        to_call = self.type_map.get(query_type, None)
        if not to_call:
            raise RequestFailure("Query type is not supported.")
        if query_type == 'ip':
            params = {'ip': query}
        elif query_type == 'network':
            params = {'cidr': query}
        elif query_type == 'port':
            params = {'port': query}
        else:
            params = {'asn': query}
        return self._request(to_call, params=params)
