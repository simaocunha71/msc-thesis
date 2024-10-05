    var result int = 1
    var temp int = n

    for temp != 0 {
        digit := temp % 10
        if digit%2 != 0 {
            result *= digit
        }
        temp /= 10
    }

    return result
}



// 测试用例
func ExampleDigits() {
    fmt.Println(Digits(1))             // 1
    fmt.Println(Digits(4))             // 0
    fmt.Println(Digits(235))           // 15
    fmt.Println(Digits(9999999999999999)) // 9
}



// 解题思路：
// 1. 将输入的整数拆分成每一个数字
// 2. 遍历每一个数字，如果是奇数，就将其与result相乘，并将结果保存到result中
// 3. 如果所有数字都是偶数，那么result将始终为1
// 4. 最后返回result

// 解题步骤：
// 1. 将输入的整数拆分成每一个数字
// 2. 遍历每一个数字，如果是奇数，就将其与result相乘，并将结果保存到result中
// 3. 如果所有数字都是偶数，那么result将始终为1
// 4. 最后返回result

// 解题代码：
import (
    "strconv"
)

// Given a positive integer n, return the product of the odd Digits.
// Return 0 if all Digits are even.
// For example:
// Digits(1)  == 1
// Digits(4)  == 0
// Digits(235) == 15
func Digits(n int) int {

    var result int = 1
    var temp int = n

    for temp != 0 {
        digit := temp % 