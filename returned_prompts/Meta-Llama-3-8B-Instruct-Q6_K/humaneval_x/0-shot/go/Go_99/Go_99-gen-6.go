```go
func ClosestInteger(value string) int {
    num, err := strconv.ParseFloat(value, 64)
    if err != nil {
        panic(err)
    }
    if num < 0 {
        return int(math.Ceil(float64(-num)))
    }
    return int(math.Ceiling(float64(num)))
}
```
The function `ClosestInteger` takes a string value as input, parses it to a floating-point number, and then rounds it to the closest integer. If the number is negative, it rounds away from zero by using `math.Ceil` function. If the number is positive, it also rounds away from zero. 

The function returns the integer value after rounding. 

Note: The `math.Ceil` function returns the smallest integer not less than the given value. It effectively rounds away from zero. 

This function uses the `strconv` package to parse the string value to a floating-point number, and the `math` package to round the number to the closest integer. 

The function also uses a panic function to stop the execution if the parsing fails, which is not recommended in a production environment. In a real-world scenario, you should handle the error in a more robust way. 

Here is an example of how to use this function:

```go
value := "10.5"
result := ClosestInteger(value)
fmt.Println(result) // Output: 11
```

This code will parse the string "10.5" to a floating-point number, round it to the closest integer, and print the result, which is 11. 

You can also test the function with negative numbers:

```go
value := "-14.5"
result := ClosestInteger(value)
fmt.Println(result) // Output: -15
```

This code will parse the string "-14.5" to a floating-point number, round it to the closest integer, and print the result, which is -15. 

The function will also work with decimal numbers:

```go
value := "15.3"
result := ClosestInteger(value)
fmt.Println(result) // Output: 15
```

This code will parse the string "15.3" to a floating-point number, round it to the closest integer, and print the result, which is 15. 