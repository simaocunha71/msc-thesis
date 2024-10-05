```go
func Multiply(a, b int) int {
    return int(math.Abs(int(math.Mod(float64(a), 10))) * math.Abs(int(math.Mod(float64(b), 10))))
}
```



Explanation:
The problem asks to write a function that takes two integers and returns the product of their unit digits. For example, the unit digits of 148 and 412 are 8 and 2, and their product is 16.

Here's the solution:
```go
func Multiply(a, b int) int {
    return int(math.Abs(int(math.Mod(float64(a), 10))) * math.Abs(int(math.Mod(float64(b), 10))))
}
```
This function uses the `math.Mod` function to get the remainder of the input numbers when divided by 10, which gives the unit digits. The `math.Abs` function is used to get the absolute value of the unit digits, and then the product is calculated and returned.

For example, if the input is 148 and 412, the function will return the product of the unit digits 8 and 2, which is 16. If the input is 19 and 28, the function will return the product of the unit digits 9 and 8, which is 72. If the input is 2020 and 1851, the function will return the product of the unit digits 0 and 1, which is 0. If the input is 14 and -15, the function will return the product of the unit digits 4 and 5, which is 20.