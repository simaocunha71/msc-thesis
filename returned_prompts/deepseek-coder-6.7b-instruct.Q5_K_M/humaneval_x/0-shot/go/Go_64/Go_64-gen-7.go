    count := 0
    s = strings.ToLower(s)
    for _, c := range s {
        switch c {
        case 'a', 'e', 'i', 'o', 'u':
            count++
        }
    }
    if s[len(s)-1] == 'y' {
        count++
    }
    return count
}
```

This program uses the `strings` package's `ToLower` function to ensure that the program is case-insensitive. It iterates over each character in the input string, and for each character, it checks whether it is a vowel by using a switch statement. If the character is a vowel, it increments the `count` variable by 1. Finally, if the last character in the string is 'y', it increments `count` by 1, and then it returns `count`.

Note: This program does not handle non-alphabet characters or strings with special characters. If you need to handle these cases, you would need to add additional error checking to the program.

Also, this program counts 'y' only at the end of the word. If you want to count 'y' as a vowel in the middle of the word, you would need to modify the program to do so.

In the example, `VowelsCount("abcde")` returns `2` because there are two vowels ('a' and 'e') in the string, and `VowelsCount("ACEDY")` returns `3` because there are three vowels ('a', 'e', and 'y') in the string.

```
```

```python
# Python Solution:

def VowelsCount(s):
    count = 0
    s = s.lower()
    for c in s:
        if c in 'aeiou':
            count += 1
    if s[-1] == 'y':
        count += 1
    return count

print(VowelsCount("abcde"))  # 2
print(VowelsCount("ACEDY"))  # 3
```

This Python program works similarly to the Go program described above. It converts the input string to lowercase, then it iterates over each character in the string. If the character