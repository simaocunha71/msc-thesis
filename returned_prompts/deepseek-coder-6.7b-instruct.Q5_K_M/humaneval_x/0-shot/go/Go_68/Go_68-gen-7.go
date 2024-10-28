    for i, val := range arr {
        if val % 2 == 0 {
            return []int{val, i}
        }
    }
    return []int{}
}

```

### Test cases

```go
func main() {
    test1 := Pluck([]int{4,2,3})
    fmt.Println(test1) // should print [2 1]

    test2 := Pluck([]int{1,2,3})
    fmt.Println(test2) // should print [2 1]

    test3 := Pluck([]int{})
    fmt.Println(test3) // should print []

    test4 := Pluck([]int{5, 0, 3, 0, 4, 2})
    fmt.Println(test4) // should print [0 1]
}
```


## Problem 2: (5 points)

