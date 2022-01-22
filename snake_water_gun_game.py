import random
def game(comp, you):
    if comp == you:
        return None
    elif comp =='s':
        if you =='w':
            return False
        elif you =='g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False
randNo = random.randint(1,3)
# print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Start game snake water or gun: ")
a = game(comp, you)

print("You choose", you)
print("computer", comp)

if a == None:
    print("The game is tie")
elif a:
    print("You Win")
else:
    print("You Lose")