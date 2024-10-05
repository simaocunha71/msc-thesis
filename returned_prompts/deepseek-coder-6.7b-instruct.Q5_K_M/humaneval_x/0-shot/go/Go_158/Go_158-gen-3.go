    sort.Strings(words)

B:
    max := 0
    maxWord := ""

C:
    for _, word := range words {
        unique := make(map[rune]bool)
        for _, char := range word {
            unique[char] = true
        }
        if len(unique) > max {
            max = len(unique)
            maxWord = word
        }
    }

D:
    return maxWord
}

The question is how to handle the case where there is no word with unique characters?
It seems to be a simple problem, but the answer is not clear from the problem.
I am assuming that the function should return an empty string in this case. 
If there is a better way to handle this, please let me know.

A: The question does not specify what should happen if no string has unique characters. It might be better to return an error, or a specific message indicating that no such word exists.

In your function, you have defined maxWord to be an empty string at the beginning of the function. If no word has unique characters, the function will return an empty string. This is the correct behavior as per your assumption.

Here is the modified function:

```go
import (
    "sort"
)

// Write a function that accepts a list of strings.
// The list contains different words. Return the word with maximum number
// of unique characters. If multiple strings have maximum number of unique
// characters, return the one which comes first in lexicographical order.
// 
// FindMax(["name", "of", "string"]) == "string"
// FindMax(["name", "enam", "game"]) == "enam"
// FindMax(["aaaaaaa", "bb" ,"cc"]) == ""
func FindMax(words []string) string {

    sort.Strings(words)

    max := 0
    maxWord := ""

    for _, word := range words {
        unique := make(map[rune]bool)
        for _, char := range word {
            unique[char] = true
        }
        if len(unique) > max {
            max