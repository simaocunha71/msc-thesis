```go
package main

import (
    "fmt"
    "sort"
)

func RemoveDuplicates(numbers []int) []int {
    m := make(map[int]bool)
    result := make([]int, 0)

    for _, value := range numbers {
        if !m[value] {
            m[value] = true
            result = append(result, value)
        }
    }

    sort.Ints(result)

    return result
}

func main() {
    fmt.Println(RemoveDuplicates([]int{1, 2, 3, 2, 4})) // Output: [1, 2, 3, 4]
}
```

Here is a brief explanation of the code:

1. We create an empty map `m` to keep track of unique elements.
2. We iterate over the input array `numbers`. For each element, we check if it's already present in the map `m`. If not, we add it to the map and append it to the result array `result`.
3. We sort the result array using the `sort.Ints` function to maintain the original order.
4. We return the result array.

This solution has a time complexity of O(n) and a space complexity of O(n), where n is the length of the input array. The space complexity is due to the map and the result array. The time complexity is due to the iteration over the input array and the sorting of the result array.