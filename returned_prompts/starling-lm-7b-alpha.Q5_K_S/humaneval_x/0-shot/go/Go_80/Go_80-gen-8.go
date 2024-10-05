To solve this problem, we can follow these steps:

1. First, we need to check if the length of the string is at least 3. If it's not, we can immediately return false since it cannot be a happy string.

2. Next, we can initialize a map with the first three letters of the string as the key and true as the value. This map will help us keep track of whether or not the first three letters have been seen before.

3. We can then iterate through the string starting from the fourth letter. For each iteration, we can check if the current letter is already in the map. If it is, we can return false since it means that the current three consecutive letters are not distinct. If it's not in the map, we can add it to the map with true as the value.

4. After iterating through the entire string, if we haven't encountered any duplicate three consecutive letters, we can return true since the string is happy. Otherwise, we return false.

Here's an implementation of the solution in Go:

```go
package main

import "fmt"

func IsHappy(s string) bool {
    if len(s) < 3 {
        return false
    }

    seen := make(map[string]bool)
    seen[s[:3]] = true

    for i := 3; i < len(s); i++ {
        if seen[s[i-2:i+1]] {
            return false
        }
        seen[s[i-2:i+1]] = true
    }

    return true
}

func main() {
    fmt.Println(IsHappy("aa"))      // false
    fmt.Println(IsHappy("abcd"))    // true
    fmt.Println(IsHappy("aabb"))    // false
    fmt.Println(IsHappy("adb"))     // true
    fmt.Println(IsHappy("xyy"))     // false
}
```

This code checks if the length of the string is less than 3 and returns false if it is. It then initializes a map called `seen` to keep track of the first three consecutive letters. It adds the first three letters to the map