    var words []string
    var result []string

    if s == "" {
        return result
    }

    words = strings.Fields(s)

    for _, word := range words {
        var consonants int
        for _, letter := range word {
            if strings.ContainsRune("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ", letter) {
                consonants++
            }
        }
        if consonants == n {
            result = append(result, word)
        }
    }
    return result
}

In the code above, I first check if the input string is empty. If it is, I return an empty list.
Then I split the string into words using the `strings.Fields` function.
For each word, I count the number of consonants. If the count of consonants equals the input number n, I add the word to the result list.
Finally, I return the result list.

This code works by iterating over each character in the word and checking if it is a consonant. If it is, I increment the consonants counter. If the counter equals the input number n, I append the word to the result list.

The time complexity of this code is O(n*m), where n is the number of words in the string and m is the average length of the words. The space complexity is O(n), as I store the words in a list and the result in a separate list.

