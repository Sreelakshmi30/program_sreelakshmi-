#first and last character exchange#

def change_sring(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]
	  
print(change_sring('python'))
print(change_sring('12345'))
