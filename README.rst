Python Netinfo
==============
.. image:: https://readthedocs.org/projects/netinfo/badge/?version=latest
    :target: https://netinfo.readthedocs.io/en/latest/?badge=latest

.. image:: https://badge.fury.io/py/netinfo.svg
    :target: https://badge.fury.io/py/netinfo

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://opensource.org/licenses/MIT

This is an abstract python library built on top of the `Netinfo`_ service. It is preferred that users use this library when implementing integrations or plan to use Netinfo within their code. The library includes a small client to interact with the API.

.. _Netinfo: https://github.com/9b/netinfo

Quick Start
-----------
**Install the library**:

``pip install  netinfo`` or ``python setup.py install``

**Ensure you are running a local Netinfo service**:

**Perform enrichment**

``netinfo enrich -q 74.96.94.146 -t ip``


Features
--------
* Wrapper to call endpoints from Netinfo

Changelog
---------
02-14-19
~~~~~~~~
* Initial release