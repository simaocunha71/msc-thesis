
def larg_nnum(lst, n):
    lst.sort(reverse=True)
    return lst[:n]

print(set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)))

# Alternative Solution

def largest_n_numbers(lst, n):
    return sorted(lst, reverse=True)[:n]

print(set(largest_n_numbers([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)))
<jupyter_output>
{100, 90}
{100, 90}
<jupyter_text>
10. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.Note: Use 'continue' statement.
<jupyter_code>
# Solution

for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i)
<jupyter_output>
0
1
2
4
5
<jupyter_text>
11. Write a Python program that accepts a string and calculate the number of digits and letters.
<jupyter_code>
# Solution

s = input("Enter a string: ")
d = 0 # count for digits
l = 0 # count for letters

for char in s:
    if char.isdigit():
        d += 1
    elif char.isalpha():
        l += 1

print("Number of digits: ", d)
print("Number of letters: ", l)
<jupyter_output>
Enter a string:  hello123
Number of digits:  3
Number of letters:  5
<jupyter_text>
12. Write a Python program that accepts a string and calculate the number of uppercase letters,