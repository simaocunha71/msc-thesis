To solve this problem, you can follow these steps:

1. First, check if the length of the string is less than 3. If it is, return false because the string cannot have 3 consecutive distinct letters.
2. Next, create a set to store the characters we've seen. This set will help us quickly check if a character has been seen before.
3. Iterate through the string, taking groups of 3 characters at a time. For each group, check if all characters are distinct. If any character is repeated, return false.
4. If all groups of 3 characters are distinct, return true.

Here's a code example that implements these steps:

```go
package main

import "fmt"

func IsHappy(s string) bool {
    if len(s) < 3 {
        return false
    }
    seen := make(map[byte]bool)
    for i := 0; i < len(s)-2; i++ {
        if _, exists := seen[s[i]]; exists {
            return false
        } else {
            seen[s[i]] = true
        }
        if _, exists := seen[s[i+1]]; exists {
            return false
        } else {
            seen[s[i+1]] = true
        }
        if _, exists := seen[s[i+2]]; exists {
            return false
        } else {
            seen[s[i+2]] = true
        }
    }
    return true
}
```

You can test the function with the given examples:

```go
fmt.Println(IsHappy("a")) // false
fmt.Println(IsHappy("aa")) // false
fmt.Println(IsHappy("abcd")) // true
fmt.Println(IsHappy("aabb")) // false
fmt.Println(IsHappy("adb")) // true
fmt.Println(IsHappy("xyy")) // false
```

The function will return true if the string is happy (i.e., has at least 3 characters and all 3 consecutive letters are distinct) and false otherwise.

The time complexity of the function is O(n) because we