import random;

def fortuneCookie():
    fortunes = ["You are going to die in one hour","You will find one million dollars","You will be hit by a car",
                "You will find your soulmate","You will fix your code error", "Your hard drive will corrupt"]
    return random.choice(fortunes)

print(fortuneCookie())