Here's the solution for your problem:

```go
func IntToMiniRoman(number int) string {
    roman := []string{"i", "iv", "v", "ix", "x", "xl", "l", "xc", "c", "cd", "d", "cm", "m"}
    values := []int{1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000}

    result := ""
    for i := len(roman) - 1; i >= 0; i-- {
        for number >= values[i] {
            result += roman[i]
            number -= values[i]
        }
    }
    return strings.ToLower(result)
}
```

The function `IntToMiniRoman` takes an integer as an input and converts it to its Roman numeral equivalent as a string. It uses two slices, `roman` and `values`, to represent the Roman numeral symbols and their corresponding values, respectively.

The function then iterates through the `roman` slice from the end to the beginning. For each Roman numeral symbol, it checks if the input number is greater than or equal to the corresponding value. If it is, it appends the Roman numeral symbol to the result string and subtracts the value from the input number.

Finally, the function returns the result string in lowercase.