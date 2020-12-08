import sys

numbers = []

input_file = open(sys.argv[1], 'r')

#print(input_file.readline())

for x in input_file:
    numbers.append(int(x))

input_file.close()

#print(numbers)

for y in range(0,len(numbers)):
    for z in range(0,len(numbers)):
        for i in range(0,len(numbers)):
            if((numbers[y] + numbers[z]) + numbers[i] == 2020):
                answer = (numbers[y] * numbers[z]) * numbers[i]
                break

print(answer)
