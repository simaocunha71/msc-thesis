Here is a possible solution:
```go
import (
    "sort"
    "strings"
)

func SortNumbers(numbers string) string {
    // Split the input string into individual numbers
    words := strings.Split(numbers, " ")

    // Convert each word to an integer and store it in a slice
    nums := make([]int, len(words))
    for i, word := range words {
        switch word {
        case "zero":
            nums[i] = 0
        case "one":
            nums[i] = 1
        case "two":
            nums[i] = 2
        case "three":
            nums[i] = 3
        case "four":
            nums[i] = 4
        case "five":
            nums[i] = 5
        case "six":
            nums[i] = 6
        case "seven":
            nums[i] = 7
        case "eight":
            nums[i] = 8
        case "nine":
            nums[i] = 9
        }
    }

    // Sort the slice of integers
    sort.Ints(nums)

    // Convert the sorted integers back to strings and join them with spaces
    sortedWords := make([]string, len(words))
    for i, num := range nums {
        switch num {
        case 0:
            sortedWords[i] = "zero"
        case 1:
            sortedWords[i] = "one"
        case 2:
            sortedWords[i] = "two"
        case 3:
            sortedWords[i] = "three"
        case 4:
            sortedWords[i] = "four"
        case 5:
            sortedWords[i] = "five"
        case 6:
            sortedWords[i] = "six"
        case 7:
            sortedWords[i] = "seven"
        case 8:
            sortedWords[i] = "eight"
        case 9:
            sortedWords[i] = "nine"
        }
    }

    return strings.Join(sortedWords, " ")
}
```
This function first splits the input string into individual words using the `strings.Split` function. It then converts each word to an integer using a switch statement, and stores the integers in a slice. The slice is then sorted using the `sort.Ints` function. Finally, the sorted integers are converted back to strings using another switch statement, and the resulting strings are joined with spaces using the `strings.Join` function.