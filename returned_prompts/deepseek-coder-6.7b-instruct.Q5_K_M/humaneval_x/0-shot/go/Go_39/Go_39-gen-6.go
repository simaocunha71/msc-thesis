	for i := 2;;i++ {
		F:
		for j := 2; j*j <= i; j++ {
			if i%j == 0 {
				continue A
			}
		}
		if isFibonacci(i) {
			n--
			if n == 0 {
				return i
			}
		}
	}
	return -1
}

func isFibonacci(n int) bool {
	a := 0
	b := 1
	c := a + b
	for c <= n {
		if c == n {
			return true
		}
		a = b
		b = c
		c = a + b
	}
	return false
}
```

# 解説

このコードは、最初の n 個の素数と Fibonacci 数列を生成し、素数である Fibonacci 数列の n 番目を返します。

Fibonacci 数列は、前の 2 つの数の和で生成される数列です。最初の 2 つの数は 0 と 1 です。

素数とは、1 より大きく、その他の数で割り切れない整数です。

コードの `PrimeFib(n int) int` 関数は、n 番目の素数と Fibonacci 数列の数を返します。

`isFibonacci(n int) bool` 関数は、n が Fibonacci 数列であるかどうかを返します。

最初は無限ループを用意し、それを