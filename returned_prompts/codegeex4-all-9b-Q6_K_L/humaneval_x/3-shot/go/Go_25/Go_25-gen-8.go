
The first function is fine. But you could consider using a map to store the occurrences of each number. This can improve performance if the list of numbers is large, because you would not need to iterate over all numbers to find the occurrences of a specific number.

The second function has a bug. The variable current_string is a slice of runes, but when you append a rune to it, you are actually appending a single character. This means that the resulting strings will contain single characters, not groups of parentheses. To fix this, you should append the rune to a string instead of a slice of runes.

The third function is fine. But you could consider using a loop that starts from the square root of the number, rather than from 2. This can improve performance if the number is large, because you would not need to iterate over all numbers to find the factors of a specific number.