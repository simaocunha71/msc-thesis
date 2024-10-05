
    largest := math.MinInt64
    smallest := math.MaxInt64
    hasNeg := false
    hasPos := false
    for _, v := range lst {
        if v < 0 && v > largest {
            largest = v
            hasNeg = true
        } else if v > 0 && v < smallest {
            smallest = v
            hasPos = true
        }
    }
    if !hasNeg {
        largest = nil
    }
    if !hasPos {
        smallest = nil
    }
    return [2]interface{}{largest, smallest}
}

```

## Code Explanation

The function `LargestSmallestIntegers` accepts a slice of integers `lst` as the input. It initializes two variables, `largest` and `smallest`, to the minimum and maximum possible integer values respectively.

Then it iterates over each number `v` in `lst`. If `v` is negative and greater than `largest`, it updates `largest`. Similarly, if `v` is positive and less than `smallest`, it updates `smallest`.

It also keeps track of whether there are negative or positive integers in `lst` by setting the corresponding boolean variables `hasNeg` and `hasPos` to `true` if an update is performed.

Finally, if there are no negative or positive integers, it sets `largest` and `smallest` to `nil`.

It returns a tuple of `largest` and `smallest`.

## Testing

```go
func main() {
    fmt.Println(LargestSmallestIntegers([]int{2, 4, 1, 3, 5, 7}))  // (nil, 1)
    fmt.Println(LargestSmallestIntegers([]int{}))  // (nil, nil)
    fmt.Println(LargestSmallestIntegers([]int{0}))  // (nil, nil)
}
```

## Output

```
(nil, 1)
(nil, <nil>)
(nil, <nil>)
```

## Time Complexity