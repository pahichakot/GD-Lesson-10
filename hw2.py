#This code will display the sum of the numbers in numbers.txt

numbers = []
lines = []

with open("numbers.txt", "r") as file:
    for line in file:
        numbers.append(line)
        lines.append(line)
        #print(lines)
        #print(numbers)

total = sum(int(i) for i in numbers)
print("Total :")
print(total)