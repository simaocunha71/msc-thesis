
    // Write your code here.
    // check if the intervals intersect
    if interval1[1] < interval2[0] || interval2[1] < interval1[0] {
        return "NO"
    }

    // calculate the intersection
    start := max(interval1[0], interval2[0])
    end := min(interval1[1], interval2[1])

    // calculate the length of the intersection
    length := end - start + 1

    // check if the length is a prime number
    if length < 2 {
        return "NO"
    }
    for i := 2; i*i <= length; i++ {
        if length%i == 0 {
            return "NO"
        }
    }
    return "YES"

}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

// The main function is used for testing.
func main() {
    fmt.Println(Intersection([2]int{1, 2}, [2]int{2, 3}))  // "NO"
    fmt.Println(Intersection([2]int{-1, 1}, [2]int{0, 4}))  // "NO"
    fmt.Println(Intersection([2]int{-3, -1}, [2]int{-5, 5}))  // "YES"
}

// The main function is used for testing.
func main() {
    fmt.Println(Intersection([2]int{1, 2}, [2]int{2, 3}))  // "NO"
    fmt.Println(Intersection([2]int{-1, 1}, [2]int{0, 4}))  // "NO"
    fmt.Println(Intersection([2]int{-3, -1}, [2]int{-5, 5}))  // "YES"
}


```

## 参考答案

```go
package main