    letterFrequency := map[rune]int{}
    maxFrequency := 0

    for _, letter := range test {
        letterFrequency[letter]++
        if letterFrequency[letter] > maxFrequency {
            maxFrequency = letterFrequency[letter]
        }
    }

    mostFrequentLetters := map[rune]int{}
    for letter, frequency := range letterFrequency {
        if frequency == maxFrequency {
            mostFrequentLetters[letter] = frequency
        }
    }

    return mostFrequentLetters
}


