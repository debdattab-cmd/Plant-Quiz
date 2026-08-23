print("welcome to the quiz!")
c1 = 0
c2 = 0
c3 = 0
print("Press Y to start quiz!")
ch = input()
while (ch =='y'):
    print("You have a completely free Sunday, what are you doing?")
    print("1. Spending me time with Coffee")
    print("2. Go somewhere fun and explore")
    print("3. Quietly do your own thing")
    op = int (input("Enter your choice"))
    if(op == 1):
        c1 = c1+1
    elif (op == 2):
        c2 = c2+1
    else:
        c3 = c3+1
    print("What kind of friend are you??")
    print("1. Adaptable and down for anything friend")
    print("2. Chill and Independent friend")
    print("3. Sensitive and caring friend")
    op = int (input("Enter your choice"))
    if(op == 1):
        c1 = c1+1
    elif (op == 2):
        c2 = c2+1
    else:
        c3 = c3+1
    print("Pick your favourite spot in a park")
    print("1. Under a big shady tree")
    print("2. A white bench on side of the park")
    print("3. By the fountain")
    op = int (input("Enter your choice"))
    if(op == 1):
        c1 = c1+1
    elif (op == 2):
        c2 = c2+1
    else:
        c3 = c3+1
    ch = 'n'

if (c1>c2 and c1>c3):
    print("Congratulations! you are a snake plant")
if (c2>c1 and c2>c3):
    print("Congratulations! you are a jade")
if (c3>c2 and c3>c1):
    print("Congratulations! you are a pothos")


