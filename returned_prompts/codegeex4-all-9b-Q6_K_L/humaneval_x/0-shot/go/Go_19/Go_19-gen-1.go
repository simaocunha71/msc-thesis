Here is a simple solution in Go:

```go
func SortNumbers(numbers string) string {
    numDict := map[string]int{
        "zero":   0,
        "one":    1,
        "two":    2,
        "three":  3,
        "four":   4,
        "five":   5,
        "six":    6,
        "seven":  7,
        "eight":  8,
        "nine":   9,
    }

    words := strings.Fields(numbers)
    ints := make([]int, len(words))
    for i, word := range words {
        ints[i] = numDict[word]
    }

    sort.Ints(ints)

    sortedNumbers := make([]string, len(ints))
    for i, num := range ints {
        for word, value := range numDict {
            if value == num {
                sortedNumbers[i] = word
            }
        }
    }

    return strings.Join(sortedNumbers, " ")
}
```

This function first creates a dictionary to map the string numbers to their corresponding integer values. Then, it splits the input string into individual words, converts them to their corresponding integer values, sorts those integers, and then converts them back to their string representations. Finally, it joins the sorted words back together into a single string and returns it.