
This function takes a string as input and returns a list of words. It first tries to split the string on whitespace using the `split()` method. If this is not successful (i.e., the string does not contain any whitespace), it then tries to split the string on commas. If this is not successful either, it counts the number of lower-case letters with odd order in the alphabet and returns this count.

Here is the breakdown of the code:

1. `words = txt.split()`: This line tries to split the input string `txt` on whitespace using the `split()` method. The resulting list of words is stored in the variable `words`.
2. `if not words and not ',' in txt`: This line checks if the `words` list is empty and if the input string `txt` does not contain any commas.
3. `return sum(1 for i in range(ord('a'), ord('z')+1) if txt.count(chr(i)) % 2 != 0)`: If the `words` list is empty and the input string `txt` does not contain any commas, this line counts the number of lower-case letters with odd order in the alphabet. It does this by iterating over the range of ASCII values for the lower-case letters (from `ord('a')` to `ord('z')+1`) and checking if the count of each letter in the input string is odd. The `sum()` function is used to add up the counts of all the letters with odd order.
4. `return words`: If the `words` list is not empty or if the input string `txt` contains commas, this line returns the `words` list. This is the default behavior if the input string can be split on whitespace or commas.

Note that this function assumes that the input string only contains ASCII characters. If the input string may contain non-ASCII characters, additional error handling may be necessary. Also, this function does not handle punctuation marks or other special characters. If the input string may contain these characters, additional processing may be necessary to correctly split the string into words.