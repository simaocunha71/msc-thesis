    // 1. 创建一个正则表达式来匹配所有的元音字母
    regex, err := regexp.Compile("[aeiouAEIOU]")
    if err != nil {
        panic(err)
    }

    // 2. 将文本中的所有元音字母替换为空字符串
    text = regex.ReplaceAllString(text, "")

    return text
}
```

**测试用例**

```go
import (
    "fmt"
    "testing"
)

func TestRemoveVowels(t *testing.T) {
    testCases := []struct {
        input    string
        expected string
    }{
        {"", ""},
        {"abcdef\nghijklm", "bcdf\nghjklm"},
        {"abcdef", "bcdf"},
        {"aaaaa", ""},
        {"aaBAA", "B"},
        {"zbcd", "zbcd"},
    }

    for _, tc := range testCases {
        t.Run(fmt.Sprintf("RemoveVowels(%s)", tc.input), func(t *testing.T) {
            got := RemoveVowels(tc.input)
            if got != tc.expected {
                t.Errorf("got %s, expected %s", got, tc.expected)
            }
        })
    }
}
```

运行测试用例，如果所有测试用例都通过，那么说明这个函数是正确的。

```go
func main() {
    TestRemoveVowels(nil)
}
```

**总结**

这是一种常见的字符串处理方法，使用正则表达式来匹配和替换字符串中的特定字符。在Go语言中，`regexp`包提供了创建和使用正则表达式的功能。

注意：在实际的代码中，我们应该处理正则表达式可能出现的错误，这里为了简洁，省略了错误处理。





















