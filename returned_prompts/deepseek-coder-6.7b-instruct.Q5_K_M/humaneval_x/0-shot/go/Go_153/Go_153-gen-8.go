    max_strength := math.MinInt64
    strongest_extension := ""
    for _, extension := range extensions {
        CAP, SM := 0, 0
        for _, char := range extension {
            if unicode.IsUpper(char) {
                CAP++
            } else if unicode.IsLower(char) {
                SM++
            }
        }
        strength := CAP - SM
        if strength > max_strength {
            max_strength = strength
            strongest_extension = extension
        }
    }
    return class_name + "." + strongest_extension
}

// END OMIT
```

## Testing

```go
func main() {
    fmt.Println(StrongestExtension("my_class", []string{"AA", "Be", "CC"}))
}
```

This program will output:
```shell
my_class.AA
```

## Explanation

In the program, we define a function `StrongestExtension` that takes two arguments: a string `class_name` and a slice of strings `extensions`. For each extension in the slice, we calculate its strength by counting the number of uppercase letters (CAP) and lowercase letters (SM). The strength of an extension is then given by the difference between CAP and SM. If the strength of an extension is greater than the current maximum strength, we update the maximum strength and store the name of the extension. Finally, we return a string in the format `class_name.strongest_extension`.

The test function `main` calls `StrongestExtension` with the example inputs and prints the result.

## Conclusion

In this program, we learned how to use Go's standard library to manipulate strings, including counting characters and finding substrings. We also learned how to compare values and update variables based on conditions.

## References

- [Go by Example: Strings](https://gobyexample.com/strings)
- [Go by Example: Ranges](https://gobyexample.com/range)
- [Go by Example: Unicode](https://gobyexample.com/strings-and-runes)
- [Go documentation: Unicode Package](https://