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

1. First, we check if `x` is greater than `y`. If it is, we return -1 because there's no even number in the range [x, y].
2. We then use a for loop to iterate over the range [x, y] inclusive.
3. For each number `i` in the range, we check if it's even by using the modulus operator `%`. If `i` is even (i.e., `i % 2 == 0`), we return `i` as the biggest even integer in the range.
4. If we reach the end of the loop without finding an even number, we return -1, indicating that there's no even number in the range [x, y].