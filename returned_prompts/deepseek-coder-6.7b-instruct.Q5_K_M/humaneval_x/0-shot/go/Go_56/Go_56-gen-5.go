
    var stack []string

    for _, b := range brackets {
        if string(b) == "<" {
            stack = append(stack, "<")
        } else {
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }

    return len(stack) == 0
}

func main()  {

    fmt.Println(CorrectBracketing("<")) // false
    fmt.Println(CorrectBracketing("<>")) // true
    fmt.Println(CorrectBracketing("<<><>>")) // true
    fmt.Println(CorrectBracketing("><<>")) // false
}

```

This code uses a stack to keep track of the opening brackets. When it encounters a closing bracket, it checks if there is a matching opening bracket in the stack. If there is, it removes it from the stack. Otherwise, it returns false. If the stack is empty at the end, it returns true, indicating that every opening bracket has a corresponding closing bracket.

This solution has a time complexity of O(n), where n is the length of the string.

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

```

```

```

```

```

```

```