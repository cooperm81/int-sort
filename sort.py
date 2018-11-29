#!/usr/bin/python
__author__ = "Mitch Cooper"
__copyright__ = "Copyright 2018, Mitch Cooper"
__license__ = "Apache"
__version__ = "1.0"
__maintainer__ = "Mitch Cooper"
__email__ = "mitchell.d.cooper@gmail.com"
__status__ = "Production"

import logging
import sys
import random


logging.basicConfig(stream=sys.stdout, level=logging.ERROR)

def printArray ( a ):   
    print( "list contains {} item(s)".format(len(a)) )
    for i in range(0, len(a)):
        print( "---> item {}:{}".format(i,str(a[i])) )
    return 0

def sortIntArray( unsorted ):
    new = []
    i = 0

    if (len(unsorted) <= 1):
        return unsorted

    # looking for the first item to put into new[]
    while ((len(new) == 0) and len(unsorted) >= 1):
        tosort = unsorted.pop()
        # checking if the value coming out of the array is actually an int
        try:
            assert type(tosort) == int, "expected integer value and received non-integer value"
        except AssertionError:
            logging.warning("found non-integer value {} in array, skipping it".format(tosort))
        else:
            logging.debug("inserting {} at position {}".format(tosort, str(i)))
            new.insert(i, tosort)
    
    # there's at least something in the new list, so we need to compare to find the right location to insert
    while (len(unsorted) >= 1):
        logging.debug( "still {} item(s) to sort".format(len(unsorted)) )

        # there is still at least one item in the list
        tosort = unsorted.pop()

        # checking if the value coming out of the array is actually an int
        try:
            assert type(tosort) == int, "expected integer value and received non-integer value"
        except AssertionError:
            logging.warning("found non-integer value {} in array, skipping it".format(tosort))
            continue

        i = 0
        logging.debug( "considering item {}".format(tosort) )

        # loop through until finding an entry >= tosort
        if ( tosort >= new[len(new)-1] ):
            # it's the largest item, append
            logging.debug("appending \"{}\" at end ".format(tosort) )
            new.append( tosort )
            i = len(new)
        while (i < len(new)):
            logging.debug("considering if \"{}\" is <= \"{}\"".format(tosort, new[i]))
            if (tosort > new[i]):
                logging.debug("no")
                i += 1
            else:
                logging.debug("yes, inserting \"{}\" at position ".format(tosort, str(i)))
                new.insert(i, tosort)
                break
    return new

def createArray( size ):
    a = []
    MAX_NUMBER = 1000

    for i in range(0,size):
        n = random.randint(0,MAX_NUMBER)
        a.append(n)
    
    return a

def main():
    size = 1000
    original = [ 4, 5, 4, 11, 98, 0, 2, 3, 7, 'x', 444 ]
    #original = createArray ( size )
    printArray( original )
    printArray( sortIntArray( original ) )

    return 0


if (__name__ == "__main__"):
    main()