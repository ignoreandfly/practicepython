import random

lowercase_letters= list('abcdefghijklmnopqrstuvwxyz')
uppercase_letters = list('abcdefghijklmnopqrstuvwxyz'.upper())
numbers = list('0123456789')
special_characters = list('~! @#$%^&*()_-+={[}]|\:;<,>.?/')

password_generator = random.sample(lowercase_letters, random.randint(1,10))+random.sample(uppercase_letters, random.randint(1,10))+ random.sample(numbers, random.randint(1,10))+random.sample(special_characters, random.randint(1,10))
random.shuffle(password_generator)

print("".join(password_generator))