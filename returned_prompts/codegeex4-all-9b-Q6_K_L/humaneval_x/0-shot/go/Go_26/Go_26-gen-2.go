You can use a map to keep track of the occurrences of each number in the list. Then, iterate over the list again and append only the numbers that have a count of 1 to a new slice. Here's how you can implement this in Go:

```go
func RemoveDuplicates(numbers []int) []int {
    counts := make(map[int]int)
    for _, num := range numbers {
        counts[num]++
    }

    result := make([]int, 0)
    for _, num := range numbers {
        if counts[num] == 1 {
            result = append(result, num)
        }
    }

    return result
}
```

This function first creates a map called `counts` to store the count of each number in the input list. Then, it iterates over the list again and appends only the numbers that have a count of 1 to a new slice called `result`. Finally, it returns the `result` slice containing only the numbers that occur once in the input list.

You can test this function with the provided example:

```go
func main() {
    numbers := []int{1, 2, 3, 2, 4}
    result := RemoveDuplicates(numbers)
    fmt.Println(result) // Output: [1 3 4]
}
```

This will output `[1 3 4]`, which is the expected result.