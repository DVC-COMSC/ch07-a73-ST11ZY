

numbers = [5, 20, 30, 35, 50]

insval = int(input('Enter the insertion value: '))
# ******************************
# Make your Code
# ******************************
for i in range(len(numbers)):
    if numbers[i-1]<insval and numbers[i]>insval:
        numbers.insert(i,insval)
print(numbers)