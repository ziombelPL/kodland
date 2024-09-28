import random
znaki = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
dlugosc = int(input("Jaka ma być długość hasła: "))
haslo = [None] * dlugosc
for i in range(dlugosc):
    haslo[i] = random.choice(znaki)
haslo_str = ''.join(haslo)
print("Twoje hasło to:", haslo_str)