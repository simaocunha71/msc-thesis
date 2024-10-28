    var result string
    maxCount := 0

    for _, w := range words {
        set := make(map[rune]bool)
        for _, c := range w {
            set[c] = true
        }
        count := len(set)
        if count > maxCount {
            maxCount = count
            result = w
        } else if count == maxCount {
            if w < result {
                result = w
            }
        }
    }
    return result
}





My Answer:

func FindMax(words []string) string {
    max := ""
    for _, word := range words {
        if len(word) == len(setToCount(word)) {
            if word < max {
                max = word
            }
        }
    }
    return max
}

func setToCount(word string) string {
    var set map[rune]bool = make(map[rune]bool)
    for _, c := range word {
        set[c] = true
    }
    var result string = ""
    for k := range set {
        result += string(k)
    }
    return result
}




Explanation:
My solution is O(n*log(n)) because sorting a string is O(n*log(n)).
The solution by @kostix is O(n) because the sorting is O(n).

In my solution, I'm converting each word to a string of unique characters, then comparing the length of the original word and the length of the string of unique characters.
If the length are the same, I compare the two strings and the one that comes first lexicographically is the one with more unique characters.

In the setToCount function, I'm making a map of unique characters, then converting it to a string.











































































