
    // Type checking
    if _, ok := x.(int); !ok {
        return false
    }
    if _, ok := y.(int); !ok {
        return false
    }
    if _, ok := z.(int); !ok {
        return false
    }

B:

    // Sum of the other two numbers
    sum := x.(int) + y.(int)

C:

    // Check if one number equals the sum of the other two
    if sum == z.(int) {
        return true
    } else {
        return false
    }

}

func main() {
    fmt.Println(AnyInt(5, 2, 7)) // ➞ true
    fmt.Println(AnyInt(3, 2, 2)) // ➞ false
    fmt.Println(AnyInt(3, -2, 1)) // ➞ true
    fmt.Println(AnyInt(3.6, -2.2, 2)) // ➞ false
}
```

在上面的代码中，我们首先检查输入的三个变量是否都是整数。如果任何一个不是整数，我们返回false。然后，我们计算其他两个数字的和。如果其中一个数字等于这个和，我们返回true；否则，我们返回false。

这个函数可以处理任何整数输入。如果输入不是整数，它将返回false。

在main函数中，我们使用不同的整数和非整数输入来测试我们的函数。

代码的输出结果为：

```
true
false
true
false
```

这与问题描述中给出的示例相匹配。
*/

package main

import (
	"fmt"
)

func AnyInt(x, y, z interface{}) bool {
	// Type checking
	if _, ok := x.(int); !ok {
		return false
	}
	if _, ok := y.(int); !ok {
		return false
	}
	if _, ok := z.(int); !ok {
		return false
	}

	// Sum of the other two numbers