#Display a pyramid with step accepted from user#

rows=int(input("enter rows :"))
for i in range(1,rows):
    for j in range(1,i+1):
        print(i*j ,end='  ')
    print("  ")