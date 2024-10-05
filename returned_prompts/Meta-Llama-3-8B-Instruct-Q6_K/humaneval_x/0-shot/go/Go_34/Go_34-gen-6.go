```go
package main

import (
    "fmt"
    "sort"
)

func Unique(l []int) []int {
    // Create a map to store unique elements
    m := make(map[int]bool)
    unique := []int{}

    // Iterate over the list
    for _, v := range l {
        // If the element is not present in the map, add it to the map and unique slice
        if _, value := m[v]; !value {
            m[v] = true
            unique = append(unique, v)
        }
    }

    // Sort the unique slice
    sort.Ints(unique)

    return unique
}

func main() {
    l := []int{5, 3, 5, 2, 3, 3, 9, 0, 123}
    fmt.Println(Unique(l))
}
```

Output:
```
[0 2 3 5 9 123]
```

Explanation:
The `Unique` function takes a slice of integers `l` as an argument. It first creates a map `m` to store unique elements. Then, it iterates over the list and checks if each element is present in the map. If it's not present, it adds the element to the map and the `unique` slice. Finally, it sorts the `unique` slice and returns it.

In the `main` function, we create a sample list `l` and call the `Unique` function with it. The output is the sorted unique elements in the list.