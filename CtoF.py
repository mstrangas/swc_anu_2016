#!/usr/bin/env python

from sys import argv

def celsius_to_fahr(temp_c):
    temp_f =(temp_c * (9.0/5.0)) + 32 
    return temp_f

def dowork():
	try:
		celc =float(argv[1])
		print celsius_to_fahr(celc)

	except:
		print "no good, try again"


if __name__ == "__main__":
	dowork()



