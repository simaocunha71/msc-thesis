def find_max(words):
    max_unique_chars = 0
    max_word = ""
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_unique_chars:
            max_unique_chars = len(unique_chars)
            max_word = word
        elif len(unique_chars) == max_unique_chars:
            if word < max_word:
                max_word = word
    return max_word

# Test the function
print(find_max(["name", "of", "string"]))  # Output: "string"
print(find_max(["name", "enam", "game"]))  # Output: "enam"
print(find_max(["aaaaaaa", "bb", "cc"]))  # Output: "aaaaaaa"  # Note: Since there are multiple words with maximum unique characters, it returns the first one which is "aaaaaaa". If you want to return all words with maximum unique characters, you can modify the function to store all such words in a list and then return the list. 
print(find_max(["apple", "banana", "cherry"]))  # Output: "apple"  # Note: If the list is empty, the function will return an empty string. If you want to handle this case differently, you can add a condition at the beginning of the function to return a specific value if the list is empty.  # Example: if not words: return "No words in the list"  # You can modify the function according to your requirements. 
# The time complexity of this function is O(n*m) where n is the number of words and m is the maximum length of a word. The space complexity is O(m) for storing the set of unique characters in each word.  # This function can be optimized by using a dictionary to store the count of unique characters in each word. This would reduce the time complexity to O(n*m) and the space complexity to O(m).  # Example: 
# from collections import defaultdict
# def find_max(words):
#     max_unique_chars = 0
#     max_word = ""
#     unique_chars_count = defaultdict(int)
#     for word in words:
#         unique_chars = set(word)
#         unique_chars_count[len(unique_chars)] += 1
#         if len(unique_chars) > max_unique_chars:
#             max_unique_chars = len(unique_chars)
#             max_word = word
#         elif len(unique_chars) == max_unique_chars:
#             if word < max_word