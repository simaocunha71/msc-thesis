
	return 0;
}

```

## 解答

```go
package main

import "fmt"

func Modp(n int, p int) int {
	res := 1
	for i := 0; i < n; i++ {
		res = (res * 2) % p
	}
	return res
}

func main() {
	fmt.Println(Modp(3, 5))  // 3
	fmt.Println(Modp(1101, 101))  // 2
	fmt.Println(Modp(0, 101))  // 1
	fmt.Println(Modp(3, 11))  // 8
	fmt.Println(Modp(100, 101))  // 1
}
```

在这个解答中，我们使用了一个简单的数学性质，即 `(a * b) mod p = ((a mod p) * (b mod p)) mod p`。我们使用这个性质来计算 `2^n`，并在每一步计算 `mod p`，从而避免了大数计算的可能性。

函数 `Modp(n int, p int) int` 接受两个整数 `n` 和 `p` 作为输入，并返回 `2^n` 对 `p` 取模的结果。

在 `main` 函数中，我们使用了一些测试用例来测试我们的函数。

请注意，这个函数只处理非负的 `n` 和 `p`。如果 `n` 是负数或 `p` 是非正数，你可能需要使用其他函数或库来处理这些情况。

另外，这个函数使用了循环来计算 `2^n` 对 `p` 取模的结果。如果 `n` 非常大，那么这个循环可能会变得非常慢。在这种情况下，你可能需要使用其他算法来更快地计算结果。

最后，这个函数使用了整数溢出来处理大数。如果你处理的是非常大的数，你可能需要使用其他数据类型来避免整数溢出。

希望