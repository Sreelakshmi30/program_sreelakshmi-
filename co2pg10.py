#generate all factors of a number#

n=int(input("enter no:"))
print("factor is:")
for i in range(1,n+1):
    if n%i==0:
        print(i)