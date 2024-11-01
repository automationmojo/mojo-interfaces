"""
.. module:: ibasiccredential
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains the `IBasicCredential` protocol object which defines the properties
               of a basic credential.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2024, Myron W Walker"
__credits__ = []


from typing import Any, Dict, Protocol

class IBasicCredential(Protocol):

    @property
    def username(self) -> str:
        """
            The username associated with the credential
        """
    
    @property
    def password(self) -> str:
        """
            The password assciated with the credential
        """
