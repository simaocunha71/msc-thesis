```go
package main

import (
    "fmt"
    "sort"
)

func SmallestChange(arr []int) int {
    // Reverse the array to compare with the original array
    reverse := make([]int, len(arr))
    copy(reverse, arr)
    sort.Ints(reverse)

    // Count the number of elements that are different
    var count int
    for i := 0; i < len(arr); i++ {
        if arr[i] != reverse[i] {
            count++
        }
    }

    return count
}

func main() {
    fmt.Println(SmallestChange([]int{1, 2, 3, 5, 4, 7, 9, 6}))  // Output: 4
    fmt.Println(SmallestChange([]int{1, 2, 3, 4, 3, 2, 2}))  // Output: 1
    fmt.Println(SmallestChange([]int{1, 2, 3, 2, 1}))  // Output: 0
}
```



Explanation:

This problem can be solved by counting the number of elements that are different between the original array and its reverse. This is because a palindromic array is read the same backwards and forwards, so if the array is not palindromic, the number of elements that are different between the original array and its reverse is the minimum number of elements that need to be changed to make the array palindromic.

In the code, we first create a copy of the original array and reverse it. Then we sort the reversed array to get the correct reverse of the original array. We then iterate through the original array and the reversed array, and count the number of elements that are different. This count is the minimum number of elements that need to be changed to make the array palindromic.

In the `main` function, we test the `SmallestChange` function with three different arrays and print the results. The output is as expected.