import sys

for line in sys.stdin:
	#new added edges 
	linesplit=line.split("\t")

	print "{}\t1".format(linesplit[0])