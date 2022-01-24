import random
n = random. randint(0,100) 
#print(n)
print("Please enter an integer between 0 and 100 : ")
nn = int(input())
while nn!=n:
    if nn>n:
        print('lower')
    else:
        print('higher')
    nn = int(input())
print ("Congratulations ! The random number was", nn)
