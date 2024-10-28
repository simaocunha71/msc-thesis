
    var count int
    for _, num := range nums {
        if num > 10 {
            str := strconv.Itoa(num)
            if str[0] % 2 == 1 && str[len(str)-1] % 2 == 1 {
                count++
            }
        }
    }
    return count
}

*/
package main

import (
	"fmt"
	"strconv"
)

func Specialfilter(nums []int) int {
	var count int
	for _, num := range nums {
		if num > 10 {
			str := strconv.Itoa(num)
			if str[0]%2 == 1 && str[len(str)-1]%2 == 1 {
				count++
			}
		}
	}
	return count
}

func main() {
	fmt.Println(Specialfilter([]int{15, -73, 14, -15})) // Expected output 1
	fmt.Println(Specialfilter([]int{33, -2, -3, 45, 21, 109})) // Expected output 2
}
package main

import (
	"fmt"
	"math"
)

func main() {
	n := 5
	result := generate(n)
	fmt.Println(result)
}

func generate(n int) [][]int {
	res := make([][]int, 0)
	if n == 0 {
		return res
	}
	res = append(res, []int{1})
	if n == 1 {
		return res
	}
	res = append(res, []int{1, 1})
	if n == 2 {
		return res
	}
	for i := 3; i <= n; i++ {
		row := make([]int, i)
		prevRow := res[len(res)-1]
		row[0] = 1
		row[len(row)-1] = 1
		for j := 1; j < len(row)-1; j++ {
			row