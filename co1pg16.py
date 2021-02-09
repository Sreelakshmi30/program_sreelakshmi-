#swapping character at position 1#

str1=input("Enter string1 : ")
str2=input("Enter string2 : ")
temp=str1[0]
str1=str1.replace(str1[0],str2[0])
str2=str2.replace(str2[0],temp)
print(str1,str2)