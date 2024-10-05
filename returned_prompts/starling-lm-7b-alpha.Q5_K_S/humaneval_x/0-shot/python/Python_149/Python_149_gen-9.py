
def sorted_list_sum(lst):
    # Create an empty list to store the strings with even length
    even_length_strings = []

    # Iterate through the list and append the strings with even length to the new list
    for string in lst:
        if len(string) % 2 == 0:
            even_length_strings.append(string)

    # Sort the list of strings by length and alphabetically
    even_length_strings.sort(key = lambda x: (len(x), x))

    return even_length_strings

# Test the function
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]


Here is a detailed explanation of the solution:

The function `sorted_list_sum` takes a list of strings as a parameter. It creates an empty list called `even_length_strings` to store the strings with even length.

Then, it iterates through the input list using a for loop. For each string in the list, it checks if its length is divisible by 2 (i.e., if it has an even length). If the length is even, it appends the string to the `even_length_strings` list.

After iterating through all the strings, the function sorts the `even_length_strings` list using the `sort` method. The `key` parameter of the `sort` method is set to a lambda function that returns a tuple of two values for each string: its length and the string itself. This ensures that the list is first sorted by length in ascending order, and then alphabetically in case of ties in length.

Finally, the function returns the sorted `even_length_strings` list.

The test cases provided at the end of the solution demonstrate the functionality of the `sorted_list_sum` function by asserting that it correctly handles different scenarios.

Overall, this solution effectively deletes the strings with odd lengths from the input list and returns the resulted list sorted by ascending length and alphabetically in case of ties in length.














