
    def by_length(arr):
        # Define number to word dictionary
        num_to_word = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}

        # Filter array for integers between 1 and 9 inclusive
        arr = [i for i in arr if isinstance(i, int) and 1 <= i <= 9]

        # Sort and reverse the array
        arr = sorted(arr, reverse=True)

        # Replace each digit by its corresponding name
        arr = [num_to_word[i] for i in arr]

        return arr

# Test cases
print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))  # ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
print(by_length([]))  # []
print(by_length([1, -1, 55]))  # ['One']
print(by_length([8, 5, 1, 4, 2, 2, 9, 3, 'a', 0, 7, 6]))  # ["Eight", "Five", "Four", "Three", "Two", "Two", "Nine", "One"]
<jupyter_output>
['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
[]
['One']
['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'Nine', 'One']
<jupyter_text>
Problem 3:
<jupyter_code>
