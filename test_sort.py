#!/usr/bin/python

import unittest
import sort

class myModuleTest(unittest.TestCase):
    
    def test_sortIntArray(self):
        # basic happy test
        myArray = [ 2, 4, 1, 3, 5 ]        
        assert(sort.sortIntArray( myArray ) == [ 1, 2, 3, 4, 5 ])
        # myArray = [ 2, 4, 1, 3, 'x' ]        
        # assert(sort.sortIntArray( myArray ) == [ 1, 2, 3, 4, 5 ])

if (__name__ == "__main__"):
    unittest.main()