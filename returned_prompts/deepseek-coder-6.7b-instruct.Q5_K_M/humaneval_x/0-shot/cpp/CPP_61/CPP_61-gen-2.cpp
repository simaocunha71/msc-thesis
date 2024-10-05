    int count = 0;
    for(char c : brackets){
        if(c == '(') count++;
        if(c == ')') count--;
        if(count < 0) return false;
    }
    return count == 0;
}

int main(){
    printf("%d\n", correct_bracketing("("));
    printf("%d\n", correct_bracketing("()"));
    printf("%d\n", correct_bracketing("(()())"));
    printf("%d\n", correct_bracketing(")(()"));
    return 0;
}

```

### 思路

我们遍历字符串`brackets`中的每个字符，并根据字符是'('还是')'来增加或减少一个计数器。

如果我们遇到一个')'，但没有匹配的'('，那么计数器就会减少，从而将计数器变为负数。

如果计数器最终不为零（即有未匹配的'('），则返回false。

否则，返回true。

### 复杂度分析

- 时间复杂度：O(n)，其中n是字符串的长度。我们只遍历一次字符串。
- 空间复杂度：O(1)，因为我们只使用一个变量来跟踪计数器。

### 参考链接

- [LeetCode](https://leetcode.com/problems/valid-parentheses/)

## 问题：有效的括号

给定一个只包含 '(' 和 ')' 的字符串，判断它是否是有效的括号字符串。

### 示例

```
输入: "()"
输出: true

输入: "()[]{}"
输出: true

输入: "(]"
输出: false

输入: "([)]"
输出: false

输入: "{[]}"
输出: true
```

### 思路

我们可以使用一个计数器来跟踪括号的数量。如果我们遇到一个开括号，我们增加计数器；如果我们遇到一个闭括号，我们减少计数器。如果