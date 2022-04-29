#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

password_length = 12
possible_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"

random_character_list = [random.choice(possible_characters) 
                         for i in range(password_length)]
random_password = "".join(random_character_list)

print("Would you like to receive a random password or input your own password(y or n): ")
ans = input()

if ans=="y":
    print(random_password)
elif ans=="n":
    print("Enter password: ")
    password = input()
    print("Saving...\nPassword has been saved")


# In[ ]:





# In[ ]:




