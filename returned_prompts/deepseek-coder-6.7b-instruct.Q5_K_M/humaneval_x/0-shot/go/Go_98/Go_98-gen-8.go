    upper := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count := 0

    for i := 0; i < len(s); i += 2 {
        if strings.ContainsRune(upper, rune(s[i])) {
            count++
        }
    }

    return count
}

```

## 3. 使用 Go 测试函数

在 Go 中，通常使用 "testing" 包来测试函数。下面是 CountUpper 函数的测试代码：

```go
import (
    "testing"
)

func TestCountUpper(t *testing.T) {
    if CountUpper("aBCdEf") != 1 {
        t.Error("Expected 1")
    }

    if CountUpper("abcdefg") != 0 {
        t.Error("Expected 0")
    }

    if CountUpper("dBBE") != 0 {
        t.Error("Expected 0")
    }
}
```

在这个测试函数中，我们使用 t.Error 来报告错误，如果 CountUpper 函数的结果与预期不符。

## 4. 运行测试

在终端中，你可以运行以下命令来运行测试：

```bash
go test
```

如果所有测试都通过，你应该看到类似于以下的输出：

```bash
PASS
ok      command-line-arguments  0.001s
```

如果有任何测试失败，你会看到类似于以下的输出，并列出失败的测试和错误消息：

```bash
--- FAIL: TestCountUpper (0.00s)
    count_upper_test.go:10: Expected 0, got 1
FAIL
exit status 1
FAIL    command-line-arguments  0.001s
```

在这种情况下，我们看到第一个测试失败了，因为我们期望 CountUpper 函数在字符串 "aBCdEf" 中返回 1，但它返回了 0。

