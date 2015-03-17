import sys

cYear=None
#cLines=[]

for line in sys.stdin:
	#line=line.strip("\n")
	[year,u,v]=line.split("\t")
	cYear=year
	resultLine="{}\t{}".format(u,v)
	#print resultLine
	f=open("./series/"+cYear+".txt","a")
	f.writelines([resultLine])

# f=open("./series/"+cYear+".txt","w+")
# print resultLine
# f.writelines([resultLine])
