```go
func Fib(n int) int {
	if n <= 1 {
		return n
	}
	return Fib(n-1) + Fib(n-2)
}
```
B:
```go
func Fib(n int) int {
	if n < 1 {
		return 0
	}
	if n == 1 {
		return 1
	}
	if n == 2 {
		return 1
	}
	return Fib(n-1) + Fib(n-2)
}
```
C:
```go
func Fib(n int) int {
	if n < 0 {
		return 0
	}
	return Fib(n-1) + Fib(n-2)
}
```
D:
```go
func Fib(n int) int {
	if n <= 0 {
		return 0
	}
	return Fib(n-1) + Fib(n-2)
}
```
E:
```go
func Fib(n int) int {
	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}
	return Fib(n-1) + Fib(n-2)
}
```
F:
```go
func Fib(n int) int {
	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}
	if n == 2 {
		return 1
	}
	return Fib(n-1) + Fib(n-2)
}
```