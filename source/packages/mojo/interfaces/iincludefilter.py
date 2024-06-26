"""
.. module:: iincludefilter
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains a protocol for determining if an item should be included in
               a list.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []


from typing import Any, List, Protocol

class IIncludeFilter(Protocol):
    """
        The IIncludeFilter interface is used to provide a common interface for performing an
        include filter on objects.
    """

    def should_include(self, check_object: Any) -> bool:
        """
            Determines if a device matches an include criteria internalized in the filter object.

            :param check_object: The object to check for a match with the exclude criteria.
        """
    
    def filter(self, input_list: List[Any]) -> List[Any]:
        """
            Processes an input list and returns a list filtered based on the results
            of calls to the `should_include` method.

            :param input_list: List of items to filter.

            :returns: A filtered copy of the input list.
        """
        output_list = []

        for nxt_object in input_list:
            if self.should_include(nxt_object):
                output_list.append(nxt_object)

        return output_list
