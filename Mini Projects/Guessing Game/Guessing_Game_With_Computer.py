import random


def compguess(lowval, highval, randnum, count=0):
    if highval >= lowval:
        guess = lowval+(highval-lowval)//2
        if guess == randnum:
            return count
        elif guess > randnum:
            count += 1
            return compguess(lowval, guess-1, randnum, count)
        else:
            count += 1
            return compguess(guess+1, highval, randnum, count)


randnum = random.randint(1, 100)
count = 0
guess = 0
print("\n\n\t\t\tWelcome To The GUESSING GAME Developed by @Satyam Tripathi")
while guess != randnum:
    guess = int(input("\nPlease Guess the No. b/w 1 & 100: "))
    if guess > randnum:
        print("You Guess \"Higher No.\" !")
    elif guess < randnum:
        print("You Guess \"Lower No.\" !")
    else:
        print("Greate!, You guess the No. $$$")
    count += 1
print(f"You took: {count} Chances !")
print(f"Computer took: {compguess(0,100,randnum)} Chances !")
