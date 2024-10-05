    words := strings.Fields(s)
    vowels := "aeiouAEIOU"
    result := []string{}

    for _, word := range words {
        count := 0
        for _, char := range word {
            if !strings.ContainsRune(vowels, char) {
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
    fmt.Println(SelectWords("Mary had a little lamb", 4)) // should print [little]
    fmt.Println(SelectWords("Mary had a little lamb", 3)) // should print [Mary lamb]
    fmt.Println(SelectWords("simple white space", 2)) // should print []
    fmt.Println(SelectWords("Hello world", 4)) // should print [world]
    fmt.Println(SelectWords("Uncle sam", 3)) // should print [Uncle]
}

I:
In the above code, we first split the input string s into words using the Fields function from the strings package. Then, for each word, we count the number of consonants by iterating over the characters in the word and checking if the character is not a vowel (i.e., it is not present in the string of vowels). If the count of consonants equals n, we append the word to the result list. Finally, we return the result list.

The time complexity of this function is O(n*m), where n is the number of words in the string and m is the average length of the words. The space complexity is O(k), where k is the number of words with exactly n consonants.

Note that the Fields function from the strings package splits the string s into words based on spaces, and the ContainsRune function checks if a rune is present in a string.

Also, the strings in the examples are case-sensitive, so "Mary" is considered a word with 3 consonants, not 4.

The function will return an empty list if the string is empty.

The function is case-sensitive, so "Mary