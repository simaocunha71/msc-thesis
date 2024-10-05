    var start int = max(interval1[0], interval2[0])
    var end int = min(interval1[1], interval2[1])

    if (start > end) {
        return "NO"
    }

    if (end - start + 1 > 2) {
        return "NO"
    }

    if (end - start + 1 == 1) {
        return "YES"
    }

    if (end - start + 1 == 2) {
        if ((start + end) % 2 == 0) {
            return "NO"
        } else {
            return "YES"
        }
    }
    return "NO"
}

func max(i1, i2 int) int {
    if (i1 > i2) {
        return i1
    } else {
        return i2
    }
}

func min(i1, i2 int) int {
    if (i1 < i2) {
        return i1
    } else {
        return i2
    }
}

*/
import "fmt"
func main() {
    fmt.Println(Intersection([2]int{1, 3}, [2]int{2, 4}))
    fmt.Println(Intersection([2]int{-1, 1}, [2]int{0, 4}))
    fmt.Println(Intersection([2]int{-3, -1}, [2]int{-5, 5}))
}

```
here is a solution to the problem

```go
package main

import "fmt"

func main() {
    fmt.Println(Intersection([2]int{1, 3}, [2]int{2, 4}))
    fmt.Println(Intersection([2]int{-1, 1}, [2]int{0, 4}))
    fmt.Println(Intersection([2]int{-3, -1}, [2]int{-5, 5}))
}

func Intersection(interval1 [2]int, interval2 [2]int) string {
    var start int = max(