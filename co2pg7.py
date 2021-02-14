#add ing at the end of a given string.If it is already ends with ing then add ly#

string=input("enter a string:")
if len(string)<3:
    print(string)
elif string[-3:]=='ing':
    print(string+'ly')
else:
    print(string+'ing')