
    // check length of the string
    if len(s) < 3 {
        return false
    }

    // iterate over the string
    for i := 0; i < len(s)-2; i++ {

        // check if 3 consecutive letters are distinct
        if s[i] == s[i+1] || s[i+1] == s[i+2] || s[i] == s[i+2] {
            return false
        }
    }

    return true
}

// Test the function
func main() {

    fmt.Println(IsHappy("a"))       // should return false
    fmt.Println(IsHappy("aa"))      // should return false
    fmt.Println(IsHappy("abcd"))    // should return true
    fmt.Println(IsHappy("aabb"))    // should return false
    fmt.Println(IsHappy("adb"))     // should return true
    fmt.Println(IsHappy("xyy"))     // should return false
}

```

This program works by first checking if the length of the string is less than 3. If it is, it returns false. Then it goes through the string and checks if any 3 consecutive letters are the same. If it finds any, it returns false. If it doesn't find any, it returns true.

This program is correct and efficient. It has a time complexity of O(n) because it needs to go through the string once. The space complexity is O(1) because it only uses a constant amount of space.


## Output:

```
false
false
true
false
true
false
```

As expected, the function IsHappy returns true for strings where every 3 consecutive letters are distinct, and false otherwise.





































































































