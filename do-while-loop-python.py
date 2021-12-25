>>>import random
magic_number = random.randint(1,20)

attempts = 0

while attempts<5:
       
        print("Guess a number between 1 and 20:")
        guess = int(input())
        attempts = attempts + 1
        
        if guess == magic_number:
           break
        
print("You have guessed the magic number!")