# from a list of vowels selected from a given word #

w=input("Enter a word:")
c=len(w)
s=1
for i in range(1,c):
    if w[i]=="":
           s+=1
print("Number of vowels are",s)        