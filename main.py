

numbers = [5, 20, 30, 35, 50]

insval = int(input('Enter the insertion value: '))
# ******************************
# Make your Code
# ******************************
for i in range(len(numbers)):
    if numbers[i-1]<insval and numbers[i]>insval:
        numbers.insert(i,insval)
        break
    if numbers[i]>insval:
        numbers.insert(i,insval)
        break
    if numbers[4]<insval:
        numbers.insert(5,insval)
        break
print(numbers)