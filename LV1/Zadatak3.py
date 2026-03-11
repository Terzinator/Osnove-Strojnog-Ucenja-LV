
numbers = []

while(True):
    a=input("Input a number")
    
    if(a.upper()=="DONE"):
        break
    
    try:
        a = int(a)
        numbers.append(a)
    except:
        print("Not a number")

print('You input ', len(numbers), ' numbers')
print('Average: ', float(sum(numbers)/len(numbers)))
print('Max: ', max(numbers))
print('Min: ', min(numbers))
numbers.sort()
print(numbers)
