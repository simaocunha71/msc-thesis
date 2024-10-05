
To determine if a string is happy, we need to check the following conditions:
1. The length of the string should be at least 3.
2. Every 3 consecutive letters should be distinct.

Here's a step-by-step guide on how to implement the solution in Go:

1. Define a function called "IsHappy" that takes a string as input and returns a boolean value.
2. Check if the length of the string is less than 3. If it is, return false, as the string is not happy.
3. Iterate through the string in chunks of 3 letters. For each chunk, check if all the letters are distinct. If any two letters are the same, return false, as the string is not happy.
4. If all the conditions are met, return true, indicating that the string is happy.

Here's an example implementation of the solution in Go:

```go
package main

import "fmt"

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
    fmt.Println(IsHappy("adb"))  // true
    fmt.Println(IsHappy("aabb")) // false
}
```

By following these steps, you can determine if a given string is happy or not based on the conditions specified.

Hope this helps!

```go
```

```
```
```

```
```
```
```

```
```
```
```
```
```

```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
``