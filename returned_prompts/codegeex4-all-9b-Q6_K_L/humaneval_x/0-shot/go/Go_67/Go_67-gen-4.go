```go
func FruitDistribution(s string, n int) int {
	split := strings.Split(s, " ")
	apples, _ := strconv.Atoi(split[0])
	oranges, _ := strconv.Atoi(split[4])
	return n - apples - oranges
}
```
这个函数可以正确计算芒果的数量，但是有几点需要改进：

1. 在尝试将字符串转换为整数时，我们没有处理可能发生的错误。如果字符串不能转换为整数，`strconv.Atoi` 函数将返回一个错误，但我们的函数没有处理这个错误。

2. 我们没有检查字符串是否包含预期的格式。如果字符串的格式与预期的格式不匹配，例如字符串中没有找到两个数字，我们的函数将无法正确工作。

3. 我们假设字符串中的数字总是以 "apples" 和 "oranges" 作为分隔符。如果字符串的格式不同，我们的函数将无法正确工作。

为了改进这个函数，我们可以添加错误处理和格式检查，以确保我们的函数可以正确处理各种输入。以下是改进后的函数：

```go
import (
	"strconv"
	"strings"
)

func FruitDistribution(s string, n int) (int, error) {
	// 检查字符串是否包含预期的格式
	if !strings.Contains(s, "apples") || !strings.Contains(s, "oranges") {
		return 0, fmt.Errorf("Invalid input format")
	}

	// 将字符串分割为单词
	split := strings.Split(s, " ")

	// 查找 "apples" 和 "oranges" 的索引
	applesIndex := -1
	orangesIndex := -1
	for i, word := range split {
		if word == "apples" {
			applesIndex = i
		} else if word == "oranges" {
			orangesIndex = i
		}
	}

	// 检查是否找到了 "apples" 和 "oranges"
	if applesIndex == -1 || orangesIndex == -1 {
		return 0, fmt.Errorf("Invalid input format")
	}

	// 提取数字
	apples, err := strconv.Atoi(split[applesIndex-1])
	if err != nil {
		return 0, fmt.Errorf("Invalid input format")
	}

	oranges, err := strconv.Atoi(split[orangesIndex-1])
	if err != nil {
		return 0, fmt.Errorf("Invalid input format")
	}

	// 计算芒果的数量
	mangoes := n - apples -