    var w []string
    var c int
    for _, r := range strings.Fields(s) {
        c = 0
        for _, v := range r {
            if !strings.Contains("aeiou", string(v)) {
                c++
            }
            if c == n {
                w = append(w, r)
                break
            }
        }
    }
    return w
}

I don't understand the part of `c++` and `break` in for loop.

The function `SelectWords` counts the number of consonants in each word and break the loop when the count is equal to `n`.

Here is a step-by-step walkthrough for the input `"Mary had a little lamb"` and `n = 4`:

```go
s := "Mary had a little lamb"
n := 4

w := []string{}                    // The result words
c := 0                             // The current count of consonants

for _, r := range strings.Fields(s) {
    c = 0                          // Reset the count for the current word
    for _, v := range r {
        if !strings.Contains("aeiou", string(v)) {
            c++                    // Increment the count if the character is a consonant
        }
        if c == n {                // Exit the inner loop if the count is equal to `n`
            w = append(w, r)       // Add the current word to the result
            break                  // Break the inner loop
        }
    }
}
```

The inner loop iterates over each character of the current word and increments the count if the character is a consonant (i.e., not a vowel). If the count of consonants becomes equal to `n`, the inner loop is broken and the current word is added to the result. The outer loop iterates over each word in the input string.

Note that the `break` statement is used to exit the inner loop when the count of consonants becomes equal to `n` and add the current word to the result. This way, we don't need to check the count after the inner