
    def search(lst):
        count_dict = {}
        for i in lst:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        max_count = max(count_dict.values())
        for key in sorted(count_dict.keys(), reverse=True):
            if count_dict[key] >= key and key > max_count:
                return key
        return -1


    print(search([4, 1, 2, 2, 3, 1]))  # 2
    print(search([1, 2,_2, 3, 3, 3, 4, 4, 4]))  # 3
    print(search([5, 5, 4, 4, 4]))  # -1

Explanation:
The function first counts the frequency of each integer in the list and stores it in a dictionary.
Then it iterates over the keys of the dictionary sorted in descending order. For each key, it checks if its count is greater or equal to the key itself.
If it is, it returns the key. If no such key is found after iterating over all keys, it returns -1.

The time complexity of this function is O(n log n) because of the sorting operation. The space complexity is O(n) for storing the counts in the dictionary.
"""

# Code Ends Here

# Do not edit below
if __name__ == "__main__":
    try:
        print(search([4, 1, 2, 2, 3, 1]))  # 2
        print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))  # 3
        print(search([5, 5, 4, 4, 4]))  # -1
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

# Do not edit below
if __name__ == "__main__":
    try:
        print(search([4, 1, 2, 2,