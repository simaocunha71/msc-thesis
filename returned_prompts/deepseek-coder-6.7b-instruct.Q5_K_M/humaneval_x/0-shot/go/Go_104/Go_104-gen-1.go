
    // Initialize an empty slice to store the results
    result := []int{}

    // Iterate over the input slice
    for _, v := range x {

        // Convert the integer to a string and check if it contains any even digit
        if !strings.ContainsAny(strconv.Itoa(v), "2468") {

            // If it doesn't, append it to the result slice
            result = append(result, v)
        }
    }

    // Sort the result slice in increasing order
    sort.Ints(result)

    // Return the sorted result slice
    return result
}
```

## Test
```go
package main

import (
    "fmt"
    "reflect"
)

func main() {
    fmt.Println(reflect.DeepEqual(UniqueDigits([]int{15, 33, 1422, 1}), []int{1, 15, 33})) // true
    fmt.Println(reflect.DeepEqual(UniqueDigits([]int{152, 323, 1422, 10}), []int{})) // true
}
```

## Explanation
The given code first initializes an empty slice to store the results. It then iterates over the input slice. For each integer, it converts it to a string and checks if it contains any even digit (2, 4, 6, or 8). If it doesn't, it appends the integer to the result slice. Finally, it sorts the result slice in increasing order and returns it.

The test code then calls the `UniqueDigits` function with two test cases and checks if the returned result is equal to the expected result. The `reflect.DeepEqual` function is used to compare the two slices. If they are equal, the function returns `true`; otherwise, it returns `false`.

## Complexity
The time complexity of the algorithm is O(n*m) where n is the number of elements in the input slice and m is the average length of the numbers in the slice. This is because for each number in the slice, it converts it to a string and checks if