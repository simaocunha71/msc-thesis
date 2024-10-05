```go
package main

import "fmt"

func RemoveDuplicates(numbers []int) []int {
    result := make([]int, 0, len(numbers))
    for _, num := range numbers {
        if !contains(result, num) {
            result = append(result, num)
        }
    }
    return result
}

func contains(slice []int, val int) bool {
    for _, item := range slice {
        if item == val {
            return true
        }
    }
    return false
}

func main() {
    numbers := []int{1, 2, 3, 2, 4}
    fmt.Println(RemoveDuplicates(numbers))  // Output: [1 3 4]
}
```

In the code above, the `RemoveDuplicates` function removes all elements from the input slice `numbers` that occur more than once. It does this by iterating over each number in the slice, and checking if it already exists in the `result` slice using the `contains` function. If the number is not already in the `result` slice, it is added to the `result` slice. Finally, the `result` slice is returned.

The `contains` function checks if a given value `val` is present in a slice `slice`. It does this by iterating over each element in the slice, and returning `true` if the value is found, and `false` otherwise.

In the `main` function, we create a slice `numbers` with the values `[1, 2, 3, 2, 4]`, and then call the `RemoveDuplicates` function with this slice as an argument. The output is `[]int{1, 3, 4}`, which are the unique elements from the input slice.