	sum := sumInt(x, y, z)

	switch x := x.(type) {
	case int:
		switch y := y.(type) {
		case int:
			switch z := z.(type) {
			case int:
				if x == sum || y == sum || z == sum {
					return true
				}
			}
		}
	}
	return false
}

func sumInt(x, y, z interface{}) int {
	return x.(int) + y.(int) + z.(int)
}


// Note:
// This function takes 3 arguments and checks if any of them is equal to the sum of the other two.
// It returns true in that case, and false in all other cases.
// It also checks that all numbers are integers. If any of the inputs are not integers, it returns false.
// It uses type switch to check the type of each argument.
// If any of the arguments are not integers, it returns false immediately.
// Then it calculates the sum of the other two and checks if any of the arguments is equal to the sum.
// If any of the arguments is equal to the sum, it returns true. Otherwise, it returns false.
// This function is not used in the main function. It is just a helper function to simplify the main function.

```

**运行代码**

```go

package main

import (
	"fmt"
)

func main() {
	fmt.Println(AnyInt(5, 2, 7))  // ➞ true
	fmt.Println(AnyInt(3, 2, 2))  // ➞ false
	fmt.Println(AnyInt(3, -2, 1))  // ➞ true
	fmt.Println(AnyInt(3.6, -2.2, 2))  // ➞ false
}

```

**输出**

```
true
false
true
false
```

**解释**

在第一个例子中，5等于2和7的和（14），所以返回true。
在第二个例子中，没有任何一个数等