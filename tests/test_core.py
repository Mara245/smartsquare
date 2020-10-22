# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:24:28 2020

@author: client
"""


import unittest

from smartsquare.core import square

class TestCore(unittest.TestCase):
    """Unit tests for core module"""
    def test_float(self):
        """Test with floats"""
        self.assertAlmostEqual(square(2.), 4.)

if __name__ == '__main__':
    unittest.main()
