
    // Your code goes here

}

```

## 解答

```go
package main

import "fmt"

func Modp(n int, p int) int {
	if n == 0 {
		return 1
	}
	result := 1
	for i := 0; i < n; i++ {
		result *= 2
		result %= p
	}
	return result
}

func main() {
	fmt.Println(Modp(3, 5))  // 3
	fmt.Println(Modp(1101, 101)) // 2
	fmt.Println(Modp(0, 101))  // 1
	fmt.Println(Modp(3, 11))   // 8
	fmt.Println(Modp(100, 101)) // 1
}

```

## 运行代码

你可以将代码复制粘贴到在线的 Go 编译器中运行。

## 解释

在 `Modp` 函数中，我们首先处理了 `n` 等于 0 的边界情况。在这种情况下，函数应该返回模 p 下的 1。

然后我们使用一个循环，将 `result` 变量乘以 2。在每次乘法之后，我们取模 p，以确保结果保持在模 p 下。这相当于将数字限制在某个范围内，而不超过它。

循环运行 `n` 次，因此 `result` 最终是 2^n 模 p。

函数然后返回这个值。

在 `main` 函数中，我们使用各种输入调用 `Modp` 函数，并打印结果。

这个解决方案的时间复杂度是 O(n)，因为有 n 次乘法运算。空间复杂度是 O(1)，因为我们只使用了固定数量的变量。

## 注意

这个解决方案假设 n 是非负数，p 是正数。如果 p 是 1，那么根据数学约定，结果是未定义的。

