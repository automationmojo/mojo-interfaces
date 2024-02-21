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
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"


from typing import Any, Dict, Protocol

class ISerializable(Protocol):

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        ...

    def as_dict(self) -> Dict[str, Any]:
        ...
