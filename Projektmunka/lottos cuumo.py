import random

# Bekérjük az öt számot
user_numbers = []
for i in range(5):
    while True:
        try:
            number = int(input(f"Kérlek adj meg egy {i+1}. számot (1-90 között): "))
            if 1 <= number <= 90 and number not in user_numbers:
                user_numbers.append(number)
                break
            else:
                print("Érvénytelen szám. Az érvényes tartomány 1-90, és minden szám csak egyszer használható.")
        except ValueError:
            print("Érvénytelen bemenet. Kérlek adj meg egy érvényes számot.")

# Sorsolás
lotto_numbers = random.sample(range(1, 6), 5)

# Találatok számolása
hits = len(set(user_numbers).intersection(lotto_numbers))
if hits == 5:
    print("Nyertél")
# Eredmény 
print(f"A te számaid: {sorted(user_numbers)}")
print(f"A lottó nyerőszámai: {sorted(lotto_numbers)}")
print(f"Találataid száma: {hits}")
if hits >= 3:
    print("Nyertél")
