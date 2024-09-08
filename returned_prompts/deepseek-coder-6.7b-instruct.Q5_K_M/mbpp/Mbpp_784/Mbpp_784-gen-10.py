
def mul_even_odd(nums):
    even_product = 1
    odd_product = 1
    for num in nums:
        if num % 2 == 0:
            even_product *= num
        else:
            odd_product *= num
    return even_product, odd_product

even, odd = mul_even_odd([1,3,5,7,4,1,6,8])
print(even, odd)

# Output: 192 1155
<jupyter_output>
192 1155
<jupyter_text>
Q2:Write a Python program that asks the user to enter their age and then prints a message to say whether they are old enough to vote or not.
<jupyter_code>
age = int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
<jupyter_output>
Enter your age: 21
You are eligible to vote.
<jupyter_text>
Q3:Write a Python program that asks the user for a number and then prints out a list of all the divisors of that number.
<jupyter_code>
num = int(input("Enter a number: "))
divisors = [i for i in range(1, num + 1) if num % i == 0]
print(divisors)
<jupyter_output>
Enter a number: 15
[1, 3, 5, 15]
<jupyter_text>
Q4:Write a Python program that will ask the user for a string and print out whether this string is a palindrome or not.
<jupyter_code>
string = input("Enter a string: ")
reverse_string = string[::-1]
if string == reverse_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
<jupyter_output>
Enter a string: level
The string is a