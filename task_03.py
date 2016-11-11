#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """custom file logger"""

    def __init__(self, logfilename):
        """log file name"""
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """log file msg and timestamp"""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """flush messages"""
        handled = []
        try:
            fhandler = open(self.logfilename, 'a')
        except IOError:
            self.log('cannot open log file')
            raise IOError

        for index, entry in enumerate(self.msgs):
            try:
                fhandler.write(str(entry) + '\n')
                handled.append(index)
            except IOError:
                self.log('cannot write to log file')
                break

        fhandler.close()

        for index in handled[::-1]:
            if handled[::1] is IOError:
                pass
            else:
                del self.msgs[index]
