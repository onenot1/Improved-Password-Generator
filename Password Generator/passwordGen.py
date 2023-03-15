import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1,2,3,4,5,6,7,8,9,0]

def Generate(length):
    password = ""
    for x in range(length):
        randomLetter = alphabet[random.randint(0, len(alphabet)-1)]
        randomUppercaseChance = random.random()
        randomNumberChance = random.random()
        if randomUppercaseChance > 0.8:
            password += randomLetter.upper()
        elif randomNumberChance > 0.75:
            password += str(numbers[random.randint(0, len(numbers)-1)])
        else:
            password += randomLetter.lower()
    return password

