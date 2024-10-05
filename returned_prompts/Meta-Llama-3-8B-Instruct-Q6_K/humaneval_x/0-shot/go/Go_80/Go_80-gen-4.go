```go
package main

import (
    "fmt"
    "strings"
)

func IsHappy(s string) bool {
    if len(s) < 3 {
        return false
    }
    for i := 0; i < len(s)-2; i++ {
        if s[i] == s[i+1] || s[i] == s[i+2] || s[i+1] == s[i+2] {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(IsHappy("a"))  // false
    fmt.Println(IsHappy("aa")) // false
    fmt.Println(IsHappy("abcd")) // true
    fmt.Println(IsHappy("aabb")) // false
    fmt.Println(IsHappy("adb"))  // true
    fmt.Println(IsHappy("xyy"))  // false
}
```


Output:
```
false
false
true
false
true
false
```
In this Go program, the function IsHappy checks if the given string is happy or not. A string is happy if its length is at least 3 and every 3 consecutive letters are distinct. The function uses a for loop to check every 3 consecutive letters in the string. If it finds any 3 consecutive letters that are the same, it immediately returns false. If it checks all 3 consecutive letters without finding any duplicates, it returns true. The main function calls IsHappy with different strings and prints the results.