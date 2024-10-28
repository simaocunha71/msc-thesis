
    // your code here

}


A: Here's a Python solution:

```python
def by_length(arr):
    mapping = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 
               6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    res = []
    for i in sorted(arr, reverse=True):
        if i in mapping:
            res.append(mapping[i])
    return res
```

This solution first maps the numbers 1-9 to their corresponding words. It then sorts the input array in descending order and appends the corresponding word to the result list if the number is in the mapping.

In Go, the solution can be as follows:

```go
package main

import (
    "fmt"
    "sort"
)

func ByLength(arr []int) []string {
    mapping := map[int]string{1: "One", 2: "Two", 3: "Three", 4: "Four", 
                              5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    res := []string{}
    sort.Sort(sort.Reverse(sort.IntSlice(arr)))
    for _, i := range arr {
        if val, ok := mapping[i]; ok {
            res = append(res, val)
        }
    }
    return res
}

func main() {
    arr := []int{2, 1, 1, 4, 5, 8, 2, 3}
    fmt.Println(ByLength(arr))  // prints: [Eight Five Four Three Two Two One One]
}
```

This Go solution does essentially the same thing as the Python solution. It first maps the numbers 1-9 to their corresponding words. It then sorts the input array in descending order and appends the corresponding word to the result list if the number is in the mapping.

Both solutions ignore any numbers that are