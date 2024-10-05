    var maxCount int
    var maxWord string

    for _, word := range words {
        var uniqueCount int
        seen := make(map[rune]bool)
        for _, c := range word {
            if !seen[c] {
                uniqueCount++
                seen[c] = true
            }
        }

        if uniqueCount > maxCount {
            maxCount = uniqueCount
            maxWord = word
        } else if uniqueCount == maxCount && word < maxWord {
            maxWord = word
        }
    }

    return maxWord
}




In this code, the function FindMax finds the maximum number of unique characters in a string from an array of strings. It uses a map called `seen` to keep track of whether a character has been seen before. If it has, it continues to the next character. If it hasn't, it increments the `uniqueCount` variable and adds the character to the map. After going through all the characters in a string, it checks if the `uniqueCount` is greater than the maximum `uniqueCount` seen so far. If it is, it updates the maximum `uniqueCount` and the `maxWord` to the current `word`. If the `uniqueCount` is equal to the maximum `uniqueCount`, it compares the current `word` to the `maxWord` lexicographically and updates `maxWord` if the current `word` comes first. Finally, it returns the `maxWord` with the maximum number of unique characters.










































































































































































