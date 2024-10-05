```
def histogram(test):
    if not test:
        return {}

    test = test.split()
    max_count = 0
    result = {}

    for letter in test:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
        if result[letter] > max_count:
            max_count = result[letter]

    max_count_letters = [letter for letter, count in result.items() if count == max_count]

    return {letter: count for letter, count in result.items() if letter in max_count_letters}
```


The function `histogram` takes a string `test` as an argument. It splits the string into a list of letters. Then it initializes a dictionary `result` to store the count of each letter. It also initializes a variable `max_count` to store the maximum count of a letter.

It then iterates over the list of letters. For each letter, it increments its count in the `result` dictionary. If the count of the letter is greater than `max_count`, it updates `max_count`.

After that, it creates a list `max_count_letters` that contains all letters that have the maximum count.

Finally, it returns a dictionary that contains only the letters with the maximum count. The dictionary is created using a dictionary comprehension. If a letter is not in `max_count_letters`, it is not included in the returned dictionary. If a letter is in `max_count_letters`, its count is included in the returned dictionary. If `test` is an empty string, the function returns an empty dictionary.