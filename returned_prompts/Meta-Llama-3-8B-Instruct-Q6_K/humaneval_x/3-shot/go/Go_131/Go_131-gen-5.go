    product := 1
    for _, digit := range strconv.FormatInt(int64(n), 10) {
        if digit != '0' && digit != '2' && digit != '4' && digit != '6' && digit != '8' {
            product *= int(int(digit - '0'))
        }
    }
    return product
}  // or use a regex to get the odd digits: func Digits(n int) int {
//     product := 1
//     for _, digit := range regexp.MustCompile(`[13579]`).FindAllString(strconv.Itoa(n), -1) {
//         product *= int(digit[0] - '0')
//     }
//     return product
// }  // or use a loop with math to get the odd digits: func Digits(n int) int {
//     product := 1
//     for n > 0 {
//         digit := n % 10
//         if digit % 2 != 0 {
//             product *= digit
//         }
//         n /= 10
//     }
//     return product
// }  // or use a loop with strconv to get the odd digits: func Digits(n int) int {
//     product := 1
//     for _, digit := range strconv.Itoa(n) {
//         if digit != '0' && digit != '2' && digit != '4' && digit != '6' && digit != '8' {
//             product *= int(int(digit - '0'))
//         }
//     }
//     return product
// }  // or use a loop with strings to get the odd digits: func Digits(n int) int {
//     product := 1
//     for _, digit := range []rune(strconv.Itoa(n)) {
//         if digit != '0' && digit != '2' && digit != '4' && digit != '6' && digit != '8' {
//             product *= int(int(digit - '0'))
//         }
//     }
//     return product
// }  // or use a loop with strings to get the odd digits: func Digits(n int) int {
//     product := 1
//     for _, digit := range strings.Split(strconv.Itoa(n), "") {
//         if digit != "0" && digit != "2" && digit != "4" && digit != "6" && digit !=