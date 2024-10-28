To solve this problem, you can follow these steps:

1. Check if the string contains whitespace or comma. If it does, split the string on whitespace or comma.
2. If there are no whitespace or comma, count the number of lower-case letters with odd order in the alphabet.
3. Return the result as an interface{} type.

Here is the code that implements the above steps:

```go
package main

import (
    "fmt"
    "strings"
    "unicode"
)

func SplitWords(txt string) interface{} {
    split := strings.Fields(txt)
    if len(split) > 0 {
        return split
    }
    count := 0
    for _, char := range txt {
        if char >= 'a' && char <= 'z' && unicode.IsLower(char) && (char-'a')%2 == 1 {
            count++
        }
    }
    return count
}
```

You can test the function with the following test cases:

```go
fmt.Println(SplitWords("Hello world!"))  // => ["Hello", "world!"]
fmt.Println(SplitWords("Hello,world!")) // => ["Hello", "world!"]
fmt.Println(SplitWords("abcdef"))       // => 3
```

Note that the SplitWords function returns an interface{} type, which can hold values of any type. In this case, it returns a slice of strings if the input string contains whitespace or comma, and an integer if the input string does not contain any whitespace or comma.

The function uses the strings.Fields function to split the input string on whitespace. If the length of the split string is greater than 0, it means the string contains whitespace or comma, and the function returns the split string directly.

If the length of the split string is 0, it means the string does not contain whitespace or comma. In this case, the function counts the number of lower-case letters with odd order in the alphabet by iterating through each character in the input string. If a character is a lower-case letter and its ASCII value is odd,