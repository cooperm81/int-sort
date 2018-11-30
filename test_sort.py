#!/usr/bin/python

import unittest
import sort

class myModuleTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""        

    def tearDown(self):
        """Call after every test case."""

    def test_sortIntArray(self):
        # basic happy test
        myArray = [ 2, 4, 1, 3, 5 ]        
        assert sort.sortIntArray( myArray ) == [ 1, 2, 3, 4, 5 ], "sorting 5 basic integers failed"

    def test_sortIntArray_10(self):
        '''testing arrays with non-integer values at beginning'''
        myArray = [ 'x', 2, 4, 1, 3 ]
        assert sort.sortIntArray( myArray ) == [ 1, 2, 3, 4 ], "incorrectly handled non-integer case"

    def test_sortIntArray_20(self):
        '''testing arrays with non-integer values at end'''
        myArray = [ 2, 4, 1, 3, 'x' ]
        assert sort.sortIntArray( myArray ) == [ 1, 2, 3, 4 ], "incorrectly handled non-integer case"

    def test_sortIntArray_30(self):
        '''testing arrays with non-integer values in middle'''
        myArray = [ 2, 4, 'x', 1, 3 ]
        assert sort.sortIntArray( myArray ) == [ 1, 2, 3, 4 ], "incorrectly handled non-integer case"

    def test_sortIntArray_40(self):
        '''testing large arrays'''
        a = sort.createArray(1000)
        #TODO: finish test case.

    def test_sortIntArray_50(self):
        '''testing arrays of zero length'''
        myArray = []
        assert sort.sortIntArray( myArray ) == [], "incorrectly handled zero length arrays"

    def test_sortIntArray_60(self):
        '''testing arrays with one item'''
        myArray = [ 88 ]
        assert sort.sortIntArray( myArray ) == [ 88 ], "incorrectly handled array with one item"

    def test_sortIntArray_70(self):
        '''testing arrays with one item which is non-integer'''
        myArray = [ 'hello' ]
        assert sort.sortIntArray( myArray ) == [], "incorrectly handled array with one item that is non-integer"

if (__name__ == "__main__"):
    unittest.main() #run all test cases