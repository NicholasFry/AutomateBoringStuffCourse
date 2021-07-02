# spam = True
# myAge = 35
# print(myAge < 30)
# myDog = 'jimmy'
# print(myAge > 20 and myDog == 'jimmy')
# name = "Alice"
# if name == "Alice":
#     print("Hi Alice")
# print("Done.")
###Part 3
# password = 'swordfish'
# if password == 'swordfish':
#     print('access granted.')
# else:
#     print('wrong password pal.')
###Part 4
# name = "Bob"
# age = 3000
# if name == 'Alice':
#     print('hi Alice.')
# elif age < 12:
#     print('You are not alice')
# elif age > 2000:
#     print('You are a scary person, not alice')
# elif age > 99:
#     print('You are not alice grandma')
###Part 5
# print('enter a name')
# name = input()
# if name:
#     print('thanks for entering a name')
# else:
#     print('You did not enter a name')
####Part 6
# bool(0)#this is falsey
# bool(42)#this is truthy
# bool('hot stuff')#this is truthy
# bool('')#this is falsey
# #values 0, 0.0, and empty strings '' are considered falsey
# spam = 0
# while spam < 5:
#     print('hello world')
#     spam = spam + 1
####Part 7 Input validation using loops
# name = ''
# while name != 'your name':
#     print('Please type your name')
#     name = input()
# print('Thank you.')
####Part 8 continue checks the condition at the start of the loop
# spam = 0
# while spam < 5:
#     spam = spam + 1
#     if spam == 3:
#         continue
#     print("spam is " + str(spam))
####FOR loops
print('My name is ')
for i in range(5, 15, 4):
    print('Jimmy Five Times ' + str(i))

##count up addition to 100
# total = 0
# for num in range(101):
#     total = total + num
# print(total)
##While loop equivalent
# print('my name is ')
# i = 0
# while i < 5:
#     print('Jimmy Five Times ' + str(i))
#     i = i + 1
