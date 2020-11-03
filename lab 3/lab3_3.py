a,b,c=input("Enter the sides of Triangle :")
count=0
if a>b+c:
    print "Triangle cannot be formed!"
    count+=1
else:
    if b>a+c:
        print "Triangle cannot be formed!"
        count+=1
    
    else:
        if c>a+b:
            print "Triangle cannot be formed!"
            count+=1

        if count==0:
            print "Triangle can be formed!!!!"

    
