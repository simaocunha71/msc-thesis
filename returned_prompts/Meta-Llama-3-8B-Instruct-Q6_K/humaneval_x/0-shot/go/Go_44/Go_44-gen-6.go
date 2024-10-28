```go
func ChangeBase(x int, base int) string {
    var result string
    digits := []rune("0123456789abcdefghijklmnopqrstuvwxyz")
    for x > 0 {
        remainder := x % base
        result = string(digits[remainder]) + result
        x = x / base
    }
    return result
}
```

This function converts an integer `x` to a different base `base`. It uses the `digits` slice to get the corresponding character for each remainder when `x` is divided by `base`. The result is built by concatenating the characters in reverse order. The function returns the resulting string. Note that base 2 to 36 is supported. For base greater than 36, you will get incorrect results. If you want to support more bases, you can extend the `digits` slice accordingly. 

For example, if you want to support base 37 to 62, you can add the following characters to the `digits` slice: "ABCDEFGHIJKLMNOPQRSTUVWXYZ". 

Here is an example usage:
```go
fmt.Println(ChangeBase(8, 3)) // Output: 22
fmt.Println(ChangeBase(8, 2)) // Output: 1000
fmt.Println(ChangeBase(7, 2)) // Output: 111
```





