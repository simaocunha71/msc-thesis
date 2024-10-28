
```go
m := map[int]int{}
for _, v := range l {
    if _, ok := m[v]; ok {
        return true
    } else {
        m[0-v] = v
    }
}
return false
```

This function works by creating a map, m, that stores each element of the input list as the key and the corresponding index as the value. The function then iterates through the list and checks if the current element, v, is already in the map. If it is, then it returns true, as there are two distinct elements that sum to zero. If v is not in the map, then it adds the negative of v as a key and v as the value to the map. This process continues until all elements of the list have been processed. If no pair of distinct elements that sum to zero is found, the function returns false.

```go
package main

import "fmt"

func PairsSumToZero(l []int) bool {
    m := map[int]int{}
    for _, v := range l {
        if _, ok := m[v]; ok {
            return true
        } else {
            m[0-v] = v
        }
    }
    return false
}

func main() {
    fmt.Println(PairsSumToZero([]int{1, 3, 5, 0}))
    fmt.Println(PairsSumToZero([]int{1, 3, -2, 1}))
    fmt.Println(PairsSumToZero([]int{1, 2, 3, 7}))
    fmt.Println(PairsSumToZero([]int{2, 4, -5, 3, 5, 7}))
    fmt.Println(PairsSumToZero([]int{1}))
}
```

The expected output of the above code is:

```
false
false
false
true
false
```

The function PairsSumToZero is tested by passing different input lists to it, and the results are printed out using the fmt.Println function. The expected output shows the results of the function for each input list.

```go
package main

import "fmt