"""
.. module:: iserializable
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains the `ISerializable` protocol object which defines methods
               used to serialize and deserialize objects.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []



from typing import Any, Dict, Protocol

class ISerializable(Protocol):

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        ...

    def as_dict(self) -> Dict[str, Any]:
        ...
