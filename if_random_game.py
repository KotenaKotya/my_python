import random
rand=int(random.randint(1,4))
user=int(input("Введите число от 1 до 4:"))
if rand==user:
    print ("Победа!")
else:
    if rand > user:
        print("Рандомное число больше")
    else:
        print("Рандомное число меньше")
    
