
#display future leap years from current year to a final year entered by user#

s=2021
e = int(input("Enter end year:"))
if(s<e):
    print("Leap year are:")
    for i in range(s,e):
        if(i % 4 == 0 and i % 100 != 0 or i % 4 == 0 and i % 400 == 0):
            print(i)
        else:
                print("Invalid Year")