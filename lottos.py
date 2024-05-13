import random

numbers = []
b_field = random.randint(1,4)
while len(numbers) != 8:
  current_number = random.randint(1, 20)
  while current_number in numbers:
    current_number = random.randint(1, 20)
  numbers.append(current_number)

numbers.sort()
print("A Putto nyerőszámok:")
for x in numbers:
  print("{}".format(x), end=" ")
print("\nB mező: {}".format(b_field))