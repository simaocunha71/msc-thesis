    product := 1
    for n != 0 {
        digit := n % 10
        n /= 10
        if digit % 2 != 0 {
            product *= digit
        }
    }
    return product
}

func main()  {
    fmt.Println(Digits(1))  //== 1
    fmt.Println(Digits(4))  //== 0
    fmt.Println(Digits(235)) //== 15
}

*/

// 在Go语言中，函数的返回值必须指定。所以，你需要修改main函数，以便返回一个整数值。

package main

import (
	"fmt"
	"strconv"
)

// 给定一个正整数n，返回奇数数字的乘积。
// 如果所有数字都是偶数，则返回0。
// 例如：
// Digits(1)  == 1
// Digits(4)  == 0
// Digits(235) == 15
func Digits(n int) int {
	product := 1
	for n != 0 {
		digit := n % 10
		n /= 10
		if digit%2 != 0 {
			product *= digit
		}
	}
	return product
}

func main() {
	fmt.Println(Digits(1))   //== 1
	fmt.Println(Digits(4))   //== 0
	fmt.Println(Digits(235)) //== 15
}

// 在Go语言中，函数的返回值必须指定。所以，你需要修改main函数，以便返回一个整数值。

package main

import (
	"fmt"
	"strconv"
)

// 给定一个正整数n，返回奇数数字的乘积。
// 如果所有数字都是偶数，则返回0。
// 例如：
// Digits(1)  == 1
// Digits(4)  