
def count_digits_letters(string):
    count_letters = 0
    count_digits = 0
    for i in string:
        if i.isalpha():
            count_letters += 1
        elif i.isdigit():
            count_digits += 1
    return count_letters, count_digits

string = input("Enter a string: ")
letters, digits = count_digits_letters(string)
print(f"Letters: