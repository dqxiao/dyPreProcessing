import sys

for line in sys.stdin:
	[u,v,pTime]=line.strip("\n").split("\t")

	print "{}\t{}\t{}".format(pTime,u,v)

	