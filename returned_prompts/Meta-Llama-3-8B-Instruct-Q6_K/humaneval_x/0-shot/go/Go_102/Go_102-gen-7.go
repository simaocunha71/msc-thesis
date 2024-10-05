```go
func ChooseNum(x, y int) int {
    if x > y {
        return -1
    }
    for i := x; i <= y; i++ {
        if i%2 == 0 {
            return i
        }
    }
    return -1
}
```


Explanation:

1. First, we check if `x` is greater than `y`. If it is, we return -1 because there is no even number in the range [x, y].
2. Then, we start a loop from `x` to `y` (inclusive).
3. Inside the loop, we check if the current number `i` is even by using the modulus operator `%`. If `i` is even, we return it.
4. If the loop completes without finding an even number, we return -1.

The function works by iterating over the range [x, y] and returning the first even number it finds. If no even number is found, it returns -1. This ensures that the function always returns the largest even number in the range [x, y], or -1 if no such number exists.