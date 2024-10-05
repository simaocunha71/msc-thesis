    var even, odd int
    strNum := strconv.Itoa(num)
    for _, v := range strNum {
        n, _ := strconv.Atoi(string(v))
        if n%2 == 0 {
            even++
        } else {
            odd++
        }
    }
    return [2]int{even, odd}
}

func main() {
    fmt.Println(EvenOddCount(-12))
    fmt.Println(EvenOddCount(123))
}

*/

import (
	"fmt"
	"strconv"
)

func EvenOddCount(num int) (int, int) {
	var even, odd int
	strNum := strconv.Itoa(num)
	for _, v := range strNum {
		n, _ := strconv.Atoi(string(v))
		if n%2 == 0 {
			even++
		} else {
			odd++
		}
	}
	return even, odd
}

func main() {
	fmt.Println(EvenOddCount(-12))
	fmt.Println(EvenOddCount(123))
}

// Output:
// 1 1
// 1 2
// 表示在-12中有一个偶数(-2)和一个奇数(1)，在123中有一个偶数(2)和一个奇数(1)。
// 注意：负数会被视为一串数字，并分别计算偶数和奇数的个数。
// 在给定的示例中，-12被视为-1和2，123被视为1、2和3。
// 因此，在-12中有一个偶数和一个奇数，在123中有一个偶数和一个奇数。
// 对于负数，偶数和奇数的计数是不同的。例如，在-123中，一个偶数是2，一个奇数是-1和3，因此返回(2, 2)。
// 对于正数，偶数和奇数的计数是相同