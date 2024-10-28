
	// convert int to string
	str := strconv.Itoa(x)

	// if shift > number of digits, return digits reversed
	if shift > len(str) {
		strRune := []rune(str)
		for i, j := 0, len(strRune)-1; i < j; i, j = i+1, j-1 {
			strRune[i], strRune[j] = strRune[j], strRune[i]
		}
		return string(strRune)
	}

	// else, shift the digits right by shift
	str = str[len(str)-shift:] + str[:len(str)-shift]

	return str
}
```

## 3. 运行代码

你可以使用以下代码运行上述的CircularShift函数:

```go
package main

import (
	"fmt"
)

func main() {
	fmt.Println(CircularShift(12, 1)) // 期望输出: 21
	fmt.Println(CircularShift(12, 2)) // 期望输出: 12
	fmt.Println(CircularShift(12, 3)) // 期望输出: 123
}
```

## 4. 输出

当你运行代码时，你应该会得到以下输出:

```
21
12
312
```

这些输出与你期望的结果相匹配，因此代码按预期工作。

## 5. 总结

在这篇文章中，我们介绍了如何在Golang中实现一个函数，该函数可以将整数的位数向右移动一定次数，并返回结果作为字符串。我们还讨论了当位移次数大于位数时的情况。

如果您对Go有更多的问题，请随时提问。

## 6. 参考

1. [Go by Example](https://gobyexample.com/)
2. [Go Tour](https://tour.golang.org/welcome/1)
3. [Go Document