'''
Write a for loop that uses range() to iterate over the positions in usernames to modify the list. Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores. After running your loop, this list
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
should change to this:
usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]
'''

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here

for name in range(len(usernames)):
    usernames[name] = usernames[name].lower().replace(" ","_")
    
print(usernames)


'''
Write a for loop that iterates over the names list to create a usernames list. To create a username for each name, make everything lowercase and replace spaces with underscores. Running your for loop over the list:
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
should create the list:
usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]
'''


names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here

for name in names:
    usernames.append(name.lower().replace(" ", "_"))
    
print(usernames)