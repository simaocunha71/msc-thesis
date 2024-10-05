
// we will use a stack to solve this problem.
// we push every opening bracket to the stack and when we encounter a closing bracket, we pop the topmost element from the stack.
// if the stack is empty at the end, we return true, otherwise we return false.

    stack := []rune{}
    for _, bracket := range brackets {
        switch bracket {
        case '<':
            stack = append(stack, bracket)
        case '>':
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}

// This solution has a time complexity of O(n) where n is the length of the string and a space complexity of O(n) in the worst case when all the brackets are opening brackets.
```

## 解法

这个问题可以通过使用栈来解决。我们遍历字符串，对于每个遇到的'<'，我们将其推入栈中。如果遇到'>'，我们检查栈是否为空。如果为空，意味着没有对应的'<'，所以我们返回False。如果栈不为空，我们从栈中弹出顶部元素。如果我们遍历完整个字符串并且栈为空，我们返回True，否则返回False。

## 复杂度

这个解法的时间复杂度是O(n)，因为我们需要遍历一次字符串。空间复杂度是O(n)，在最坏的情况下，当所有括号都是开括号时，我们需要将它们全部推入栈中。

## 测试

```go
package main

import (
	"fmt"
)

func CorrectBracketing(brackets string) bool {
	stack := []rune{}
	for _, bracket := range brackets {
		switch bracket {
		case '<':
			stack = append(stack, bracket)
		case '>':
			if len(stack) == 0 {
				return false
			}
			stack = stack[:len(stack)-1]
		}
	}