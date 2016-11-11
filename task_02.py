#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """Age exception"""

    pass


def get_age(birthyear):
    """Check f age is greater than or equal to 0

    Attributes:
        birthyear (int): year to compare

    Returns:
        age (int): current year minus birthyear
        InvalidAgeError
    Example:
        >>> get_age(2099)
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>raise InvalidAgeError
        InvalidAgeError
    """

    age = datetime.datetime.now().year - birthyear
    if age >= 0:
        return age
    else:
        raise InvalidAgeError
