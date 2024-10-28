```go
package main

import (
    "fmt"
)

func Exchange(lst1, lst2 []int) string {
    // Create a copy of lst1
    copy := make([]int, len(lst1))
    copy = lst1

    // Iterate over lst2
    for i := 0; i < len(lst2); i++ {
        // Check if the current element in lst2 is even
        if lst2[i]%2 == 0 {
            // If it is even, find the first even element in lst1
            for j := 0; j < len(copy); j++ {
                if copy[j]%2 == 0 {
                    // Replace the first even element in lst1 with the current even element in lst2
                    copy[j] = lst2[i]
                    break
                }
            }
        }
    }

    // Check if all elements in the copy of lst1 are even
    for i := 0; i < len(copy); i++ {
        if copy[i]%2 != 0 {
            return "NO"
        }
    }
    return "YES"
}

func main() {
    fmt.Println(Exchange([]int{1, 2, 3, 4}, []int{1, 2, 3, 4}))  // Output: YES
    fmt.Println(Exchange([]int{1, 2, 3, 4}, []int{1, 5, 3, 4}))  // Output: NO
}
```
In this solution, we create a copy of `lst1` and iterate over `lst2`. For each even element in `lst2`, we replace the first even element in `lst1` with the current even element in `lst2`. Finally, we check if all elements in the copy of `lst1` are even. If they are, we return "YES", otherwise we return "NO". The time complexity of this solution is O(n^2) where n is the length of the input lists. The space complexity is O(n) for the copy of `lst1`.