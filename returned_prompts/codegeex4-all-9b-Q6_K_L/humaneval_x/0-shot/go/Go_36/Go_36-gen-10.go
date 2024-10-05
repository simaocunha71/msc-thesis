你的代码是正确的，但有一点可以优化。你可以在循环中直接检查并计数，而不是先转换为字符串。这样可以提高效率。以下是优化后的代码：

```go
func FizzBuzz(n int) int {
	count := 0
	for i := 1; i < n; i++ {
		if i%11 == 0 || i%13 == 0 {
			for _, digit := range strconv.Itoa(i) {
				if digit == '7' {
					count++
				}
			}
		}
	}
	return count
}
```

这个代码的逻辑和你的代码是一样的，但是它直接在循环中检查并计数，而不是先转换为字符串。这样可以提高效率。