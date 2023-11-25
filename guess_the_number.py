#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number=randint(1,100)
level=input("Choose a difficulty.Type 'easy' or 'hard':")
if level=="hard":
    attempts=5
elif level=="easy":
    attempts=10
    
while True:   
    def decrease():
        return attempts-1
    
    print(f"You have {attempts} attempts remaining to guess the number.")
    attempts=decrease()
    guess=int(input("Make a guess:"))
    
    if attempts==0:
        print("You've run out of guesses, you lose.")
        break
    if attempts!=0:
        if guess>number:
            print("Too high!")
        elif guess<number:
            print("Too low!")
        else:
            print(f"You got it! The answer was {number}.")
            break
        print("Guess again.")


# In[ ]:





# In[ ]:




