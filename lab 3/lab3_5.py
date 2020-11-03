numheads=input("Enter no of heads:")
numlegs=input("Enter no of legs:")
i=0
for i in range(numheads+1):
    j=numheads-i
    if ((2*i)+(4*j))==numlegs:
        print "Number of chickens and rabbits respectively are:"i,j

