```
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
This function first checks if the input numbers are in the correct order. If `x` is greater than `y`, it means that there is no even number within the range `[x, y]`, so the function returns `-1`.

If `x` is less than or equal to `y`, the function then iterates over the range `[x, y]` and checks each number to see if it is even. If an even number is found, the function returns that number. If no even number is found after iterating over the entire range, the function returns `-1`.

For example, if we call the function with `x = 12` and `y = 15`, the function will iterate over the range `[12, 15]` and find the even number `14`, so it will return `14`. If we call the function with `x = 13` and `y = 12`, the function will iterate over the range `[13, 12]` and find no even numbers, so it will return `-1`.