     words := strings.Split(s, " ")
     consonants := "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
     result := []string{}

     for _, word := range words {
         count := 0
         for _, char := range word {
             if strings.ContainsRune(consonants, char) {
                 count++
             }
         }
         if count == n {
             result = append(result, word)
         }
     }

     return result
 }

func main() {
    fmt.Println(SelectWords("Mary had a little lamb", 4))
    fmt.Println(SelectWords("Mary had a little lamb", 3))
    fmt.Println(SelectWords("simple white space", 2))
    fmt.Println(SelectWords("Hello world", 4))
    fmt.Println(SelectWords("Uncle sam", 3))
}

```

## Explanation
The code is first splitting the input string `s` into a list of words using the `strings.Split` function. Then it checks for every character in the words if it is a consonant by using `strings.ContainsRune` function. If a character is a consonant, it increments the count. If the count of consonants equals the input number `n`, the word is appended to the result list. Finally, the function returns the list of words that contain exactly `n` consonants.

## Test
Run this code, you will get these results:

```
[little]
[Mary lamb]
[]
[world]
[Uncle]
```

These results match the examples in the problem statement.

## Complexity
The time complexity of this solution is O(n*m), where n is the number of words in the string and m is the average length of the words. This is because for each word we iterate through its characters. The space complexity is O(n), as we store the words in a list.

## Note
This code assumes that the input string contains only letters and spaces. If the string contains punctuation or numbers