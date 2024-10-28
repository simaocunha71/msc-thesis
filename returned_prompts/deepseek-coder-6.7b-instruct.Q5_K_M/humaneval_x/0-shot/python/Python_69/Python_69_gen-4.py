
def search(lst):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    max_count_key = max(count_dict.keys())
    for key in range(max_count_key, 0, -1):
        if key in count_dict and count_dict[key] >= key:
            return key
    return -1

print(search([4, 1, 2, 2, 3, 1]))  # 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))  # 3
print(search([5, 5, 4, 4, 4]))  # -1

# The solution first calculates the frequency of each integer in the list and stores it in a dictionary. 
# Then it starts iterating from the maximum key in the dictionary to 1, and returns the first key whose 
# frequency is greater than or equal to the key itself. If no such key exists, it returns -1.
<jupyter_output>
2
3
-1
<jupyter_text>
