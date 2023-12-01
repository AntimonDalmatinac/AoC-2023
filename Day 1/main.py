#Prepare input

file = open("Day 1/input.txt", "r")
input = file.read()
file.close()

input = input.splitlines()

#Turn words into digits and create a list of lines (WHY DO THEY SHARE LETTERS, HOW INCOMPETENT ARE THESE ELVES?! Thankfully I found a hacky solution at the expense of some of my hair (I'll go bald by the end of this))

digits = {
    "zero": "zero0zero",
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine",
}

formattedLines = []

for line in input:
    for word in digits:
        line = line.replace(word, digits[word])
    formattedLines.append(line)

#Combine all digits and add them to a list

digits = []

for line in formattedLines:
    firstDigit = 0
    lastDigit = 0
    first = True
    for char in line:
        if char.isdigit():
            if first:
                firstDigit = char #We are not turning them into ints yet because we need to combine them
                lastDigit = char #According to the example, this is what you do when you only have one digit
                first = False
            else:
                lastDigit = char
    digits.append(int(firstDigit + lastDigit))

#Calculate the sum

sum = 0
for digit in digits:
    sum += digit

#Finally, print the sum/solution

print(sum)