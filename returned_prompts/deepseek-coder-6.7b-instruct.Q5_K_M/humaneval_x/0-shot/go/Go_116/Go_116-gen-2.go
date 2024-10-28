
    sort.Slice(arr, func(i, j int) bool {
        // convert the integers to their binary representation
        iBinary := fmt.Sprintf("%b", arr[i])
        jBinary := fmt.Sprintf("%b", arr[j])

        // count the number of ones in the binary representation
        iOnes := 0
        jOnes := 0
        for _, v := range iBinary {
            if v == '1' {
                iOnes++
            }
        }
        for _, v := range jBinary {
            if v == '1' {
                jOnes++
            }
        }

        // if the number of ones is the same, then sort by the decimal value
        if iOnes == jOnes {
            return arr[i] < arr[j]
        }

        // sort by the number of ones in the binary representation
        return iOnes < jOnes
    })

    return arr
}
```

This solution sorts the array by the number of ones in the binary representation of each integer first, and then by the decimal value if there are ties in the number of ones. The sort.Slice function is used to sort the array based on a custom comparison function that counts the number of ones in the binary representation of each integer and uses this count as the sort key.

This solution has a time complexity of O(n log n) because it sorts the array, where n is the length of the array. The space complexity is O(n) because it creates a new array to store the sorted result.

This solution is correct because it sorts the array as per the problem statement. It uses the standard sorting algorithm with a custom comparison function to sort the array based on the number of ones in the binary representation of each integer. If there are ties in the number of ones, it sorts based on the decimal value.

```go
package main

import (
    "fmt"
)

func main() {
    fmt.Println(SortArray([]int{1, 5, 2, 3, 4}))  // [1, 2, 3, 4, 5]
    fmt.Println(SortArray([]int{-2,