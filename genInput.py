#!/usr/bin/env python2
#
# Input file generator for saving multiple configurations for the MILC code.
# This code depends on a sample input file model.
#

from random import randint

# asks user for the number of configurations to be saved and the number of the last saved configuration.
saveNumber = int(raw_input("Enter number of desired saved configurations:"))
startConfig = int(raw_input("Enter number of last saved configuration:"))

with open('sample.in.model', 'r') as readFile:
	model = readFile.readlines()
	head = model[0:14]
	tail = model[14:30]
	readConfig = model[31].rstrip()
	writeConfig = model[32].rstrip()

with open('sample.in.file', 'w+') as writeFile:
	for line in head:
		if line.startswith('iseed'):
			writeFile.write(line.rstrip() + " " +str(randint(1000,100000)) + "\n")
		else:
			writeFile.write(line)
	for counter in range(1,saveNumber):
		for line in tail:
			writeFile.write(line)
		writeFile.write(readConfig + str(counter).zfill(4) + "\n")
		writeFile.write(writeConfig + str(counter + 1).zfill(4) + "\n")
		writeFile.write("\n")


