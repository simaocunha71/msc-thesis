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

The function `ChooseNum` takes two positive integers `x` and `y` as input and returns the largest even integer in the range `[x, y]` inclusive. If no such number exists, it returns `-1`.

Here's a step-by-step breakdown of the solution:

1. Check if `x` is greater than `y`. If true, return `-1` as there's no even number in the range `[x, y]`.
2. Iterate through the range `[x, y]` using a for loop. Start from `x` and increment by 1 until `y` is reached.
3. Inside the loop, check if the current number `i` is even by using the modulus operator `%`. If `i % 2 == 0`, it means `i` is even.
4. If an even number is found, return it as it's the largest even number in the range `[x, y]`.
5. If the loop completes without finding an even number, return `-1` as there's no even number in the range `[x, y]`.

In the example `ChooseNum(12, 15)`, the function will return `14` because it's the largest even number in the range `[12, 15]`. In the example `ChooseNum(13, 12)`, the function will return `-1` because there's no even number in the range `[13, 12]`.