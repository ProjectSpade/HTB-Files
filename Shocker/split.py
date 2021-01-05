#!/usr/bin/python3

import sys
lines_per_file = 500
smallfile = None
try:
	path = sys.argv[1]
	with open(path) as big:
		for lineno, line in enumerate(big):
			if lineno % lines_per_file == 0:
				if smallfile:
					smallfile.close()
				small_filename = 'small_file_{}.txt'.format(lineno + lines_per_file)
				smallfile = open(small_filename, "w")
			smallfile.write(line)
		if smallfile:
			smallfile.close()
except:
	print("Usage: {0} <path to file>".format(sys.argv[0]))
