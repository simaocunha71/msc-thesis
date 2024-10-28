
```go
func AnyInt(x, y, z interface{}) bool {
	var (
		xInt, yInt, zInt int
		ok               bool
	)

	if xInt, ok = x.(int); !ok {
		return false
	}

	if yInt, ok = y.(int); !ok {
		return false
	}

	if zInt, ok = z.(int); !ok {
		return false
	}

	return xInt == (yInt + zInt) || yInt == (xInt + zInt) || zInt == (xInt + yInt)
}
```

Explanation:

To solve this problem, we need to make sure all the given numbers are integers. We can use type assertion to check if the given numbers can be casted to the `int` type. If any of them can't be casted to `int`, we return `false`.

Next, we check if any of the three integers is equal to the sum of the other two. If any of them is equal to the sum of the other two, we return `true`. Otherwise, we return `false`.

In this way, we can ensure the correct result and pass the given test cases.

Note that we need to use `var` to declare multiple variables in Go.

This solution has a time complexity of O(1) and a space complexity of O(1).

Here is the Go playground for this code:

```go
func AnyInt(x, y, z interface{}) bool {
	var (
		xInt, yInt, zInt int
		ok               bool
	)

	if xInt, ok = x.(int); !ok {
		return false
	}

	if yInt, ok = y.(int); !ok {
		return false
	}

	if zInt, ok = z.(int); !ok {
		return false
	}

	return xInt == (yInt + zInt) || yInt == (xInt + zInt) || zInt == (xInt + yInt)
}
```

It's worth mentioning that this is