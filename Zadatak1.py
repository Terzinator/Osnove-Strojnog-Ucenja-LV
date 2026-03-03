def total_euro(hoursWorked, hourlyWage):
    return float(hoursWorked*hourlyWage)



print("Radnih sati: ")
hoursWorked = int(input())
print("eura/h: ")
workingWage = float(input())
print('Ukupno: ', total_euro(hoursWorked, workingWage))



