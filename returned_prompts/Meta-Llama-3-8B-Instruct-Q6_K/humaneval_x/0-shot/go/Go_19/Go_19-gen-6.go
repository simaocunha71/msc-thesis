```go
func SortNumbers(numbers string) string {
    words := strings.Split(numbers, " ")
    sort.Slice(words, func(i, j int) bool {
        switch words[i] {
        case "zero":
            return false
        case "one", "two", "three", "four", "five", "six", "seven", "eight", "nine":
            return words[i] < words[j]
        default:
            panic("Invalid number")
        }
    })
    return strings.Join(words, " ")
}
```
In this code, we first split the input string into individual words using the `strings.Split` function. Then we use the `sort.Slice` function to sort the words. The sorting function takes two indices `i` and `j` as arguments and returns `true` if the word at index `i` should come before the word at index `j`. The function checks if the word at index `i` is "zero" and returns `false` in that case, as "zero" should come last in the sorted order. If the word at index `i` is one of the numbers "one" to "nine", it compares the word with the word at index `j` using the `<` operator. If the word at index `i` is not one of the numbers "zero" to "nine", it panics with an error message. Finally, we use the `strings.Join` function to concatenate the sorted words into a single string and return it.