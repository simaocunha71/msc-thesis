    if not test:
        return {}

    histogram_dict = {}
    max_count = 0
    max_letters = []

    for letter in test.split():
        if letter in histogram_dict:
            histogram_dict[letter] += 1
        else:
            histogram_dict[letter] = 1

        if histogram_dict[letter] > max_count:
            max_count = histogram_dict[letter]
            max_letters = [letter]
        elif histogram_dict[letter] == max_count:
            max_letters.append(letter)

    return {letter: count for letter, count in histogram_dict.items() if count == max_count}  # or {letter: count for letter in max_letters for count in histogram_dict.values() if count == max_count} if you prefer this way
# This solution is using the dictionary to keep track of the letters and their counts, and then finding the maximum count. It also keeps track of the letters that have this maximum count. It returns a dictionary of these letters and their maximum count. The time complexity is O(n) where n is the length of the input string. The space complexity is also O(n) because in the worst case scenario, all letters are unique.