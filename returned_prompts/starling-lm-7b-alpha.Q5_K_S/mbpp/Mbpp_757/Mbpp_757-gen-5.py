
def count_reverse_pairs(words):
    # Reverse each word in the list
    reversed_words = [word[::-1] for word in words]

    # Create a dictionary to store the counts of reverse pairs
    reverse_counts = {}

    # Iterate through the list and add each word to the dictionary if it is a reverse pair
    for word in words:
        if word in reversed_words:
            if word not in reverse_counts:
                reverse_counts[word] = 1
            else:
                reverse_counts[word] += 1

    # Return the total count of reverse pairs
    return len(reverse_counts)


