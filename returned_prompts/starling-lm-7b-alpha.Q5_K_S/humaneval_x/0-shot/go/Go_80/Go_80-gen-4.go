To solve this problem we will follow these steps:

1. Check the length of the string, if the length is less than 3 return false.
2. Create a map to store the strings.
3. Iterate through the string and if the length is 3 or more, check if the string is present in the map or not. If it is present, return false. Else, store the string in the map.
4. Return true if the iteration is completed without any false cases.

Here is the solution:
```go
func IsHappy(s string) bool {
    if len(s) < 3 {
        return false
    }
    m := make(map[string]bool)
    for i := 0; i < len(s)-2; i++ {
        if _, ok := m[s[i:i+3]]; ok {
            return false
        } else {
            m[s[i:i+3]] = true
        }
    }
    return true
}
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

