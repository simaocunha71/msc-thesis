    // Define roman numeral symbols and their corresponding values
    vals := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
    syms := []string{"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"}

    // Initialize result string
    result := ""

    // Loop through each value in the value array
    for i := 0; i < len(vals); i++ {
        // As long as the number is greater than or equal to the current value,
        // append the corresponding symbol to the result and subtract the value from the number
        for number >= vals[i] {
            result += syms[i]
            number -= vals[i]
        }
    }

    return strings.ToLower(result)
}

```


## 2.5.5.6.1.2.3.4.5.6.7.8.9.

```go

