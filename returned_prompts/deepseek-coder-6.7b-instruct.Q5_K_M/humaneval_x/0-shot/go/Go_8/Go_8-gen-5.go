
    sum := 0
    product := 1
    
    for _, number := range numbers {
        sum += number
        product *= number
    }
    
    return [2]int{sum, product}
}

func main() {
    fmt.Println(SumProduct([]int{}))         // 应返回 [0, 1]
    fmt.Println(SumProduct([]int{1, 2, 3, 4})) // 应返回 [10, 24]
}

```

这个函数定义了两个变量`sum`和`product`，分别初始化为0和1。然后它遍历提供的切片`numbers`中的每个数字，将`sum`增加该数字的值，将`product`乘以该数字的值。最后，它返回一个包含`sum`和`product`的新切片。

在`main`函数中，它使用提供的示例调用`SumProduct`函数，并打印结果。
*/
package main

import (
	"fmt"
)

func SumProduct(numbers []int) [2]int {
	sum := 0
	product := 1

	for _, number := range numbers {
		sum += number
		product *= number
	}

	return [2]int{sum, product}
}

func main() {
	fmt.Println(SumProduct([]int{}))          // 应返回 [0, 1]
	fmt.Println(SumProduct([]int{1, 2, 3, 4})) // 应返回 [10, 24]
}
```

在上面的 Go 代码中，我们首先初始化了两个变量`sum`和`product`，并将它们分别设置为0和1。然后，我们遍历了输入切片`numbers`中的每个元素，将`sum`增加该数字的值，将`product`乘以该数字的值。最后，我们返回了一个包含`sum`和`product`的数组。

在`main`函数中，我们使用了两个测试用例