#For loop

users = ['Ed','Ana','John','Podrick','Smith']

##list Name
name = list('Edwin')
print(name)


"""
for user in users :
    print('Hello there user')
    print(user)
"""  

##Lista with Range

"""
my_list = list(range(0,10))
print(my_list)

my_list_2 = list(range(0,101))
print(my_list_2)


my_list_3 = list(range(0,101,5))
print(my_list_3)
"""

##Sample fo for with range

"""
for i in range(0,20):
    print('I run 20 times')

phrase = 'letter with capytalize'
for letter in phrase:
    print(letter)
"""

##While loop

age = 10
while age <=100 : 
    print('I am growing up')
    age = age + 1
    if(age == 14):
        print('I am independent now')
        break


