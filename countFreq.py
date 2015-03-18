import sys

cV=None
cCount=None

for line in sys.stdin:

	[u,count]=line.strip("\n").split("\t")

	if cV==None:
		cV=u
		cCount=1
	else:
		if cV==u:
			cCount+=1
		else:
			if(cCount>=2):
				print cV
			#
			cV=u
			cCount=1

if(cCount>=2):
	print cV