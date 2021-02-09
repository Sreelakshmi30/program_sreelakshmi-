#prompt the user for a list of integers.For all values greater than 100,store 'over' instead#

n=[]
s=int(input("Enter a limit:"))
print("Enter {s} values")
for i in range(0,s):
    n.append(int(input()))
print("\n The list after assigning:\n")
for i in range(0,len(n)):
    if n[i]>=100:
        print("over")
    else:
        print(n[i])