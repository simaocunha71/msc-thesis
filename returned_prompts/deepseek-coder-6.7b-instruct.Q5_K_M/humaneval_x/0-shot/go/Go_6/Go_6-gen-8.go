    result := make([]int, 0)
    groups := strings.Split(paren_string, " ")

B:
    for _, group := range groups {
        stack := make([]rune, 0)
        max_depth := 0
        current_depth := 0

C:
        for _, char := range group {
            if char == '(' {
                stack = append(stack, char)
                current_depth = len(stack)
                if current_depth > max_depth {
                    max_depth = current_depth
                }
            } else if char == ')' {
                if len(stack) > 0 {
                    stack = stack[:len(stack)-1]
                } else {
                    return nil
                }
            } else {
                return nil
            }
        }

D:
        if len(stack) != 0 {
            return nil
        }
        result = append(result, max_depth)
    }

E:
    return result
}

I've been thinking about this problem for a bit, and I'm trying to figure out why the code above is not working. The issue seems to be with the line `current_depth = len(stack)`, as the length of the stack is not being updated correctly.

Can someone point out the issue here?

A: The issue is that the length of the stack is being updated with each new '(' character, not when a ')' character is encountered.

In your code:

```
C:
    for _, char := range group {
        if char == '(' {
            stack = append(stack, char)
            current_depth = len(stack)
            if current_depth > max_depth {
                max_depth = current_depth
            }
        } else if char == ')' {
            if len(stack) > 0 {
                stack = stack[:len(stack)-1]
            } else {
                return nil
            }
        } else {
            return nil
        }
    }
```

The `current_depth = len(stack)` line is being updated on every '(' character found, not every ')' character. 
