gems=("Emerald","Ivory","Jasper","Ruby","Garnet")
prices=(1760, 2119, 1599, 3920, 3999)
n=input("Enter the gem you need:")
i=0
for i in range (0 ,5):
    if n==gems[i]:
        count=0
        count+=1
        print "Enter the number of ",gems[i],"You need :"
        q=input()
        tot_amt=q*prices[i]
        
if count==0:
    print "Gem not found!!"
    tot_amt=-1
if tot_amt>30000.00:
    tot_amt=tot_amt-(tot_amt*5/100.0)
    print "Eligible for a discount!!"
print "The bill amount is ",tot_amt,"/-"    
