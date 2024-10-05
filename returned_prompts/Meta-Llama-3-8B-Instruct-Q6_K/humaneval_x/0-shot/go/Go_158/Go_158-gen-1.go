```go
func FindMax(words []string) string {
    var maxWord string
    var maxUniqueChars int
    for _, word := range words {
        uniqueChars := len(map[string]byte{}(word))
        if uniqueChars > maxUniqueChars {
            maxUniqueChars = uniqueChars
            maxWord = word
        } else if uniqueChars == maxUniqueChars {
            if word > maxWord {
                maxWord = word
            }
        }
    }
    return maxWord
}
```


This function works by iterating over each word in the input list. For each word, it calculates the number of unique characters by converting the word to a map (which automatically removes duplicates) and then taking the length of that map. It then checks if this number of unique characters is greater than the current maximum. If it is, it updates the maximum and the word associated with that maximum. If the number of unique characters is equal to the current maximum, it checks if the word is lexicographically greater than the current maximum word. If it is, it updates the maximum word. Finally, it returns the maximum word. If no words have unique characters (i.e., they are all the same), it returns an empty string. 





This solution has a time complexity of O(N*M), where N is the number of words and M is the maximum length of a word. This is because for each word, we are iterating over its characters to count the unique characters. The space complexity is O(M), as we are storing the unique characters of each word in a map.