import random 
a= random.randint(1,100)
tries = 0
while True:
    n= int(input("tell what number i guess  between 1 to 100:-") )
    tries= tries +1
    if a==n:
        print(f"congratulations ! you won the game in {tries} tries.")
    elif a>n  and n<100:
        print("No, not that. The guessed number is higher.")
    elif a<n and n<100:
        print("No, not that. The guessed number is lower.")
    else:
        print("plese, tell between 1 to 100 only.")