#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """key or index exception error

    Attributes:
        var1 (mixed): argument variable
        var2 (mixed): argument variable
    Returns:
         LookupError: 'Warning: Your index/key doesn\'t exist.'
    Example:
        >>> simple_lookup([1,2], 4)
        Warning: Your index/key doesn't exist.
        [1,2]
        >>> simple_lookup({}, 'banana')
        Warning: Your index/key doesn't exist.
        {}
    """

    try:
        return var1[var2]
    except LookupError:
        print 'Warning: Your index/key doesn\'t exist.'
    return var1
