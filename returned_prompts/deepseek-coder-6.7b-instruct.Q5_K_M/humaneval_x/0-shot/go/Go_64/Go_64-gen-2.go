    count := 0
    s = strings.ToLower(s)
    for _, char := range s {
        switch char {
        case 'a', 'e', 'i', 'o', 'u':
            count++
        }
    }
    if s[len(s)-1] == 'y' {
        count++
    }
    return count
}
```

## Testing

To test the function, you can use the following code:

```go
package main

import (
    "fmt"
)

func main() {
    fmt.Println(VowelsCount("abcde")) // 2
    fmt.Println(VowelsCount("ACEDY")) // 3
    fmt.Println(VowelsCount("Go is fun")) // 3
    fmt.Println(VowelsCount("Why")) // 0
}
```

This code will print the number of vowels in the given strings.

## Explanation

This solution works by iterating over the input string and counting the number of vowels found. It uses the `strings.ToLower` function to make the string comparison case-insensitive.

After counting the vowels, it checks if the last character of the string is 'y'. If it is, it increments the count by 1.

Finally, it returns the count of vowels.

## Running the code

You can run the code by copying it to a `.go` file and running it with the Go compiler. Make sure to save the file with a `.go` extension and use the `go run` command in the terminal to run the file.

```bash
$ go run filename.go
```

Replace `filename.go` with the name of your file.

The code will then execute and print the number of vowels in the given strings to the console.

## Conclusion

This solution is a simple and effective way to count the number of vowels in a string in Go. It uses a for loop to iterate over the characters in the string and a switch statement to count the vowels. It also checks for the special case of 'y' at the end of the string.

Remember to import the `strings` package at the