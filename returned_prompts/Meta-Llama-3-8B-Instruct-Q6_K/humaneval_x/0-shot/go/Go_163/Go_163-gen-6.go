```
func GenerateIntegers(a, b int) []int {
    res := make([]int, 0)
    for a <= b {
        if isEven(a) {
            res = append(res, a)
        }
        a++
    }
    return res
}

func isEven(n int) bool {
    return n%2 == 0
}
```


The above code generates a slice of even numbers between the given range a and b. The function isEven is used to check if a number is even. If the number is even, it is added to the result slice. The loop runs until a becomes greater than b. The result slice is then returned.

However, there is an issue with this code. It does not handle the case when a is greater than b. We need to add a condition to handle this case.

Here is the corrected code:

```
func GenerateIntegers(a, b int) []int {
    res := make([]int, 0)
    for a <= b {
        if isEven(a) {
            res = append(res, a)
        }
        a++
    }
    for a < b {
        a--
        if isEven(a) {
            res = append(res, a)
        }
    }
    return res
}
```

In this corrected code, we added another loop after the initial loop that runs from b to a. We decrement a in each iteration and check if it is even. If it is even, we add it to the result slice. This way, we cover all even numbers between a and b, including the case when a is greater than b.