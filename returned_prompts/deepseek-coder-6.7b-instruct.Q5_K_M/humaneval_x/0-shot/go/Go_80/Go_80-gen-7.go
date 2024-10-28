
// We will be using a for loop to iterate through the string.
// Inside the loop, we will check if the current character and the next two characters are distinct.
// If they are, we will move to the next three characters.
// If they are not, we will return false.
// If we finish the loop without finding any non-distinct characters, we will return true.

// First, we check if the length of the string is less than 3.
// If it is, we return false.

	if len(s) < 3 {
		return false
	}

	for i := 0; i < len(s) - 2; i++ {
		if s[i] == s[i+1] || s[i+1] == s[i+2] || s[i] == s[i+2] {
			return false
		}
	}

	return true
}
```

## Tests

```go
package main

import (
	"fmt"
)

func main() {
	fmt.Println(IsHappy("a"))       // false
	fmt.Println(IsHappy("aa"))      // false
	fmt.Println(IsHappy("abcd"))    // true
	fmt.Println(IsHappy("aabb"))    // false
	fmt.Println(IsHappy("adb"))     // true
	fmt.Println(IsHappy("xyy"))     // false
	fmt.Println(IsHappy("abab"))    // false
	fmt.Println(IsHappy("abc"))     // true
	fmt.Println(IsHappy("aaab"))    // false
	fmt.Println(IsHappy("aabc"))    // true
	fmt.Println(IsHappy("abca"))    // false
	fmt.Println(IsHappy("abcabc"))  // true
}
```

## Explanation

This program works by iterating over the string `s` and checking if the current character and the next two characters are distinct. If they are, the function returns `false`. If it finishes the loop without finding any non-distinct characters, it returns `true`.

The time complexity of this program is O(n) because it