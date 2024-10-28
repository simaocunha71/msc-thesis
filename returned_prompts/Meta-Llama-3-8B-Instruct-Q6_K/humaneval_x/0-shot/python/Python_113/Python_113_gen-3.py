```
def odd_count(lst):
    result = []
    for i, s in enumerate(lst):
        odd_count = 0
        for digit in s:
            if int(digit) % 2 != 0:
                odd_count += 1
        result.append(f"the number of odd elements {odd_count}n the str{i+1}ng {i+1} of the {i+1}nput.")
    return result
```


Explanation:
The function `odd_count` takes a list of strings as input, where each string consists of only digits. It returns a list of strings, where each string is the count of odd digits in the corresponding input string, formatted as per the given requirements.

Inside the function, we iterate over the input list using `enumerate`, which provides both the index `i` and the value `s` of each string in the list. For each string, we initialize a variable `odd_count` to count the number of odd digits. We then iterate over each character `digit` in the string, convert it to an integer using `int(digit)`, and check if it's odd by using the modulo operator `%`. If the remainder is not zero, it means the digit is odd, so we increment `odd_count`.

After counting the odd digits, we create the output string using f-string formatting. We replace `i` with `odd_count`, and `1` with `i+1` to match the required format. Finally, we append this string to the `result` list.

The function returns the `result` list, which contains the required output strings for each input string.