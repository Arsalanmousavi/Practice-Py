string = "Whiskey Hotel Four Tango Dash Alpha Romeo Three Dash Yankee Oscar" \
         " Uniform Dash Sierra One November Kilo India November Golf Dash " \
         "Four Bravo Zero Uniform Seven"

parts = string.split(" ")

numbers = {'Zero': 0, 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
           'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Dash': '-'}

answer = []

for part in parts:

    answer.append(str(numbers.get(part, part[0])))

answer = ''.join(answer)
print(answer, type(answer))
