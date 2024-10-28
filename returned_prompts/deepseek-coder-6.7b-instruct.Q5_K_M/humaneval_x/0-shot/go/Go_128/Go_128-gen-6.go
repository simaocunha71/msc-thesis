    if len(arr) == 0 {
        return nil
    }
    
    var sum int
    var prod int = 1
    
    for _, v := range arr {
        if v > 0 {
            prod *= 1
        } else if v < 0 {
            prod *= -1
        } else {
            return 0
        }
        
        sum += int(math.Abs(float64(v)))
    }
    
    return sum * prod
}
```

## Task 2
Write a function in GoLang to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example:

    ["flower", "flow", "flight"] -> "fl"

    ["dog", "racecar", "car"] -> ""

    ["inertia", "insecure", "intentional"] -> "in"

```go
