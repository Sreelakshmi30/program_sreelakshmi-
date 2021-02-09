#list ordinal value of each element of a word#

w=input("Enter a word:")
print("Ordinal values corresponding to each element is:")
for i in w:
    print(i,end=":")
    print(ord(i),end="")