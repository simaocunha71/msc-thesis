    numWords := strings.Fields(numbers)

B:
    wordNums := map[string]string{
        "zero":  "0",
        "one":   "1",
        "two":   "2",
        "three": "3",
        "four":  "4",
        "five":  "5",
        "six":   "6",
        "seven": "7",
        "eight": "8",
        "nine":  "9",
    }

C:
    var nums []string
    for _, word := range numWords {
        nums = append(nums, wordNums[word])
    }

D:
    sort.Strings(nums)

E:
    var sortedNums []string
    for _, num := range nums {
        for word, val := range wordNums {
            if val == num {
                sortedNums = append(sortedNums, word)
                break
            }
        }
    }

F:
    return strings.Join(sortedNums, " ")
}

func main() {
    fmt.Println(SortNumbers("three one five"))
}
```

The above solution uses Go programming language and follows the steps as given in the question. It first splits the input string into a slice of words. Then it uses a map to map each word to its corresponding number. It then converts each word in the slice to its corresponding number, sorts the numbers, converts the sorted numbers back to words, and then joins them together into a space-separated string. The function `SortNumbers` returns this string. 

The time complexity of this solution is O(nlogn) because of the sorting operation. The space complexity is O(n) because of the space required to store the words, numbers, and the sorted numbers.

Note: This solution assumes that the input will always be valid. If the input can have invalid words, additional error checking would be required.


## Task 2: 

Write a Python function that accepts a string of space-separated words and returns a string of the same words, but with each word's characters reversed.