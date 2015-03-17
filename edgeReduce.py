import sys
# remove the same edge occur in differnt years 
curU=None
curV=None
firstTime=None

for line in sys.stdin:

	[u,v,ptime]=line.split("\t")
	if u==None and v==None:
		curU=u
		curV=v
		firstTime=ptime
		print line.strip("\n")
	else:
		if u!=curU or v!=curV:
			curU=u
			curV=v
			firstTime=ptime
			print line.strip("\n")

if u!=curU or v!=curV:
	print line.strip("\n")