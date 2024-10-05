    stack := []rune{}

    for _, b := range brackets {
        switch b {
        case '(':
            stack = append(stack, b) // push to stack
        case ')':
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1] // pop from stack
        }
    }

    return len(stack) == 0
}

func main() {
    fmt.Println(CorrectBracketing("("))
    fmt.Println(CorrectBracketing("()"))
    fmt.Println(CorrectBracketing("(()())"))
    fmt.Println(CorrectBracketing(")(()"))
}

```

### 运行结果

```
false
true
true
false
```

### 解释

函数`CorrectBracketing`首先初始化一个空的rune切片作为栈。然后它遍历字符串中的每个字符，如果遇到一个开括号，就将其推入栈中。如果遇到一个闭括号，并且栈为空，说明没有匹配的开括号，所以返回false。如果遇到一个闭括号，并且栈不为空，就将其从栈中弹出。如果在遍历过程中，栈不为空，说明还有未匹配的开括号，所以返回false。如果在遍历结束时，栈为空，说明所有括号都匹配，所以返回true。

在`main`函数中，我们调用`CorrectBracketing`函数并打印出结果。

## 总结

这是一种使用栈来检查括号是否匹配的常见方法。它使用了LIFO（后进先出）的原理，所以最后遇到的开括号会首先被匹配。如果遇到一个闭括号但没有对应的开括号，或者在遍历结束时还有未匹配的开括号，那么括号就不是正确的。

这种方法的时间复杂度是O(n)，其中n是字符串的长度，因为我们需要遍历整个字符串。空间复杂度