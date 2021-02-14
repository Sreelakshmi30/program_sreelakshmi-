#generate list of 4 digit numbers in a gven range with all their digits are even and the no is a perfect square#

i=int(input('enter the starting range:'))
j=int(input('enter the ending range:'))
for i in range(i,j,1):
    for j in range(32,100,1):
        if i==j*j:
           s=str(i)
           if(int(s[0])%2==0) and (int(s[1])%2==0)and(int(s[2])%2==0)and(int(s[3])%2==0):
                   print(i)
 
