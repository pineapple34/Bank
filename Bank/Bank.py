a = float(input("a - "))
years = int(input("years - "))
for i in range(0, years):
    a += a*0.1
print("Сумма - " + str(a))