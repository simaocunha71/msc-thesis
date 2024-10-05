
```go
func Add(lst []int) int {
	var sum int
	for i := 0; i < len(lst); i++ {
		if i%2 == 0 && lst[i]%2 == 0 {
			sum += lst[i]
		}
	}
	return sum
}
```

In this function, we iterate over the list and check if the index is odd and the element at that index is even. If so, we add the element to the sum. Finally, we return the sum.

Explanation:

In the function Add, we initialize a variable sum to store the sum of even elements at odd indices. We iterate over the list using a for loop and check if the index is odd (i%2 == 0) and the element at that index is even (lst[i]%2 == 0). If both conditions are true, we add the element to the sum using the += operator. Finally, we return the sum.

For example, given the list [4, 2, 6, 7], the even elements at odd indices are 4 and 6. The sum of these elements is 10, which is the value returned by the function.

To use this function, you can call it with a list of integers as an argument. For example, Add([]int{4, 2, 6, 7}) will return 10.

```go
fmt.Println(Add([]int{4, 2, 6, 7})) // Output: 10
```

This code will print the result of the function Add([]int{4, 2, 6, 7}), which is 10.

```

```

```go
```

```

```go
```

```

```go
```

```go
```

```go
```

```
```
```

```
```go
```

```go
```

```go
```

```go
```

```go
```

```go
```

