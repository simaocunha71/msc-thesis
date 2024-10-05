```go
import (
    "sort"
)

func Unique(l []int) []int {
    sort.Ints(l)
    i := 0
    for j := 1; j < len(l); j++ {
        if l[i] == l[j] {
            continue
        }
        i++
        l[i] = l[j]
    }
    return l[:i+1]
}
```
