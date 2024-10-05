    var words []string
    var res []string

    if s == "" {
        return res
    }

    words = strings.Split(s, " ")

    for _, word := range words {
        count := 0
        for _, char := range word {
            if !strings.ContainsRune("aeiouAEIOU ", char) {
                count++
            }
        }
        if count == n {
            res = append(res, word)
        }
    }
    return res
}

// main function to test the code
func main() {
    fmt.Println(SelectWords("Mary had a little lamb", 4))
    fmt.Println(SelectWords("Mary had a little lamb", 3))
    fmt.Println(SelectWords("simple white space", 2))
    fmt.Println(SelectWords("Hello world", 4))
    fmt.Println(SelectWords("Uncle sam", 3))
}

Output:
[little]
[Mary lamb]
[]
[world]
[Uncle]
```

This code is a simple solution in Go language that works as follows:

1. It first checks if the input string is empty, if it is, it returns an empty list.
2. It splits the input string into a list of words using the strings.Split function.
3. It then loops over each word in the list and counts the number of consonants using the strings.ContainsRune function.
4. If the count of consonants is equal to the input number n, it appends the word to the result list.
5. Finally, it returns the result list.

The time complexity of this solution is O(n*m), where n is the number of words in the string and m is the length of the longest word.

The space complexity is O(n) as we are storing the words in a list.

Note: This solution assumes the input string only contains letters and spaces.
*/
package main

import (
	"fmt"
	"strings"
)

func SelectWords(s string, n int) []string {
	var words []string
	var res []string

	if s == ""