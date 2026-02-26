def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
print("\n")

import random
def guess_game():
  secret = random.randint(1, 10)
  guess = int(input("Guess a number between 1 and 10: "))

  if guess == secret:
    print("You guessed it right! ")
  else:
    print("Wrong! The number was", secret)

guess_game()

