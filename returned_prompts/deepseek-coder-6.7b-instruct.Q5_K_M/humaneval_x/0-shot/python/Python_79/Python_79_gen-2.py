
    possible_characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(possible_characters) for _ in range(length))
    return random_string

print(generate_random_string(5))
print(generate_random_string(8))

# string.ascii_letters contains all the letters, string.digits contains all the digits.
# the join function is used to concatenate the random characters into a string.
# the random.choice function is used to select a random character from the possible characters.
# the function is tested with lengths of 5 and 8.
<jupyter_output>
9ZaP4
8P3Z9z4B
<jupyter_text>
5. Write a python function to find the longest common