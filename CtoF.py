#!/usr/bin/env python


import sys

def celsius_to_fahr(temp_c):
    temp_f =(temp_c * (9.0/5.0)) + 32 
    return temp_f

try:
	celc =float(sys.argv[1])
	print celsius_to_fahr(celc)

except:
	print "no good, try again"


