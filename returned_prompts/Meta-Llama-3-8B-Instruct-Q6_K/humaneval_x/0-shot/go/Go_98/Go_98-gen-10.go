```go
func CountUpper(s string) int {
    count := 0
    for i, c := range s {
        if i%2 == 0 && strings.ToUpper(string(c)) == string(c) && "AEIOU"[0] <= string(c)[0] && string(c)[0] <= "AEIOU"[4] {
            count++
        }
    }
    return count
}
```


Here is the explanation of the code:

1. Initialize a variable `count` to keep track of the count of uppercase vowels in even indices.
2. Iterate over the string `s` using the `range` keyword. The range returns the index `i` and the character `c` at that index.
3. Check if the index `i` is even using the condition `i%2 == 0`. If it is, proceed to the next step.
4. Check if the character `c` is an uppercase vowel using the conditions `strings.ToUpper(string(c)) == string(c)` and `"AEIOU"[0] <= string(c)[0] && string(c)[0] <= "AEIOU"[4]`. The first condition converts the character to uppercase and checks if it is equal to the original character, which ensures that the character is uppercase. The second condition checks if the character is one of the uppercase vowels 'A', 'E', 'I', 'O', 'U'.
5. If the character is an uppercase vowel and the index is even, increment the `count` variable.
6. Return the final value of `count`.