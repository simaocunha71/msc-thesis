```go
package main

import (
    "fmt"
)

func Exchange(lst1, lst2 []int) string {
    evenCount := 0
    for _, num := range lst1 {
        if num%2 == 0 {
            evenCount++
        }
    }
    for _, num := range lst2 {
        if num%2 == 0 {
            evenCount++
        }
    }
    if evenCount == len(lst1) {
        return "YES"
    }
    return "NO"
}

func main() {
    fmt.Println(Exchange([]int{1, 2, 3, 4}, []int{1, 2, 3, 4})) // YES
    fmt.Println(Exchange([]int{1, 2, 3, 4}, []int{1, 5, 3, 4})) // NO
}
```


Explanation:

1. Initialize a counter `evenCount` to 0.
2. Iterate through `lst1` and increment `evenCount` for each even number found.
3. Iterate through `lst2` and increment `evenCount` for each even number found.
4. If `evenCount` is equal to the length of `lst1`, return "YES" (it is possible to make all elements of `lst1` even by exchanging elements with `lst2`).
5. Otherwise, return "NO" (it is not possible to make all elements of `lst1` even by exchanging elements with `lst2`).

This solution works because it counts the total number of even numbers in both lists, and if this count is equal to the length of `lst1`, it means that all elements of `lst1` can be replaced with even numbers from `lst2`. If the count is less than the length of `lst1`, it means that there are not enough even numbers in `lst2` to replace all elements of `lst1`, so it is not possible to make all elements of `lst1` even.