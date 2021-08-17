import random
def password_generator():
    isim = input("Isminizi girin:")
    isim=isim.replace(" ", "").lower()
    part1=random.choices(isim, k=3)
    part1=part1[0]+part1[1]+part1[2]
    part2=random.choice(range(1000, 9999))
    password=part1+str(part2)
    print(password, isim)

password_generator()