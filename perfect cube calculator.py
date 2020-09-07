a=int(input("Enter a number :"))
i=2
for i in range (1,a):
    if a%i==0:
        if (a/i)==(i*i):
            print "Number is perfect cube"
            break
        else:
            print "Not perfect cube"
            
    else:
        print "Not perfect cube"
        break

