import random 
def lancamentos():
    return random.randint(1,6)

contadores= [0] * 6

for i in range (100):
    valor = lancamentos()
    contadores[valor - 1] += 1

for i in range(1, 7):
    print(f"O número {i} apareceu {contadores[i - 1]} vez(es).")
