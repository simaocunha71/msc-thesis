You can check if a list is monotonically increasing or decreasing by comparing each element with the previous one. If all elements are either increasing or decreasing, the list is monotonically increasing or decreasing respectively. Here is a solution in Go:

```go
func Monotonic(l []int) bool {
    increasing := true
    decreasing := true

    for i := 1; i < len(l); i++ {
        if l[i] < l[i-1] {
            increasing = false
        }
        if l[i] > l[i-1] {
            decreasing = false
        }
    }

    return increasing || decreasing
}
```

In this code, we first initialize two boolean variables `increasing` and `decreasing` to `true`. Then, we iterate over the list starting from the second element. In each iteration, we compare the current element with the previous one. If the current element is smaller than the previous one, we set `increasing` to `false`. If the current element is larger than the previous one, we set `decreasing` to `false`. Finally, we return `true` if either `increasing` or `decreasing` is `true`, indicating that the list is monotonically increasing or decreasing respectively.

Here are some example usages of the `Monotonic` function:

```go
fmt.Println(Monotonic([]int{1, 2, 4, 20})) // true
fmt.Println(Monotonic([]int{1, 20, 4, 10})) // false
fmt.Println(Monotonic([]int{4, 1, 0, -10})) // true
```

In the first example, the list `[1, 2, 4, 20]` is monotonically increasing, so the function returns `true`. In the second example, the list `[1, 20, 4, 10]` is not monotonically increasing or decreasing, so the function returns `false`. In the third example, the list `[4, 1, 0, -10]` is monotonically decreasing, so the function returns `true`.