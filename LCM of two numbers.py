a,b=input("Enter two numbers ")
if a<b:
    if b%a==0:
        print "LCM of ",a,"and ",b,"is ",b
    else:
        print "LCM of ",a,"and ",b,"is ",a*b
if b<a:
    if a%b==0:
        print "LCM of ",a,"and ",b,"is ",a
    else:
        print "LCM of ",a,"and ",b,"is ",a*b
