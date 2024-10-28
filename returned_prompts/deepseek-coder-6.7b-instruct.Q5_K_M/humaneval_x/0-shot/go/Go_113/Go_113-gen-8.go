    count := 0
    res := make([]string, len(lst))
    for i, str := range lst {
        for _, ch := range str {
            if int(ch-'0') % 2 != 0 {
                count++
            }
        }
        res[i] = fmt.Sprintf("the number of odd elements %don the str%dng %d of the %dnput.", count, count, i, count)
        count = 0
    }
    return res
}

*/

/*
func main() {
    res := OddCount([]string{"1234567"})
    fmt.Println(res)

    res = OddCount([]string{"3","11111111"})
    fmt.Println(res)
}
*/

// package main

// import (
// 	"fmt"
// 	"strconv"
// )

// func OddCount(lst []string) []string {
// 	res := make([]string, len(lst))
// 	for i, str := range lst {
// 		count := 0
// 		for _, ch := range str {
// 			num, _ := strconv.Atoi(string(ch))
// 			if num%2 != 0 {
// 				count++
// 			}
// 		}
// 		res[i] = fmt.Sprintf("the number of odd elements %don the string %d of the input.", count, i)
// 	}
// 	return res
// }

// func main() {
// 	res := OddCount([]string{"1234567"})
// 	fmt.Println(res)

// 	res = OddCount([]string{"3", "11111111"})
// 	fmt.Println(res)
// }

// package main

// import (
// 	"fmt"
// 	"strconv"
// )

// func OddCount(lst []string) []string {