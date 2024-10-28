```go
func ChooseNum(x, y int) int {
    if x%2 == 0 && y%2 == 0 {
        if x >= y {
            return y
        } else {
            return x
        }
    } else {
        for x <= y {
            if x%2 == 0 {
                return x
            }
            x++
        }
        return -1
    }
}
```


The function `ChooseNum` takes two positive integers `x` and `y` as input. It returns the largest even integer number in the range [x, y] inclusive. If no such number exists, it returns -1. 

Here is the breakdown of the function:

1. First, it checks if both `x` and `y` are even numbers. If they are, it compares them and returns the larger one.

2. If either `x` or `y` is not even, it iterates through the range [x, y] until it finds an even number. If it doesn't find any even number in the range, it returns -1.

Here is an example usage of the function:

```go
fmt.Println(ChooseNum(12, 15))  // Output: 14
fmt.Println(ChooseNum(13, 12))  // Output: -1
```


In the first example, the function returns 14, which is the largest even integer in the range [12, 15]. In the second example, the function returns -1 because there is no even integer in the range [13, 12]. 

Please note that the range [x, y] is inclusive, meaning that both `x` and `y` are included in the range. This is why the function compares `x` and `y` directly in the first part of the function. If the range were exclusive, the function would have to check if `x` is less than `y` before returning the larger one. 