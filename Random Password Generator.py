
# coding: utf-8

# In[ ]:


import random
character=[0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','','!','@','#','$','%','^','&','*','(',')','-','+','=','_','[','/','?','.',',']
length_of_password=input("Enter the total number of characters you want in your password ")
length=int(length_of_password)#changing the string input into integers
if length<6:
    print("Error: {} character's password will be too weak!(*it should at least be greater than 6)".format(length))
else:
    for i in range(length):
        ran_number=random.randrange(0,len(character)) #generating a random number from 0 to length of element
        print (character[ran_number],end='') #end='' done in  order to print the output in the same line

