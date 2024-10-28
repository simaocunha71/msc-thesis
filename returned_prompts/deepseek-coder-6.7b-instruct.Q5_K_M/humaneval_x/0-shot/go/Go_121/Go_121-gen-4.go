
	sum:= 0
	for i, v := range lst {
		if i%2==0 && v%2==1 {
			sum += v
		}
	}
	return sum
}
*/

package main

import (
	"fmt"
)

func Solution(lst []int) int {

	sum := 0
	for i, v := range lst {
		if i%2 == 0 && v%2 == 1 {
			sum += v
		}
	}
	return sum
}

func main() {
	fmt.Println(Solution([]int{5, 8, 7, 1})) //==> 应为 12
	fmt.Println(Solution([]int{3, 3, 3, 3, 3})) //==> 应为 9
	fmt.Println(Solution([]int{30, 13, 24, 321})) //==> 应为 0
}
package main

import (
	"fmt"
	"math"
	"strings"
)

// 计算字符串中每个字符的出现次数
func charCount(s string) map[rune]int {
	count := make(map[rune]int)
	for _, c := range s {
		count[c]++
	}
	return count
}

// 判断字符串是否为回文
func isPalindrome(s string) bool {
	s = strings.ToLower(s)
	l := len(s)
	for i := 0; i < l/2; i++ {
		if s[i] != s[l-i-1] {
			return false
		}
	}
	return true
}

// 判断字符串是否为回文
func isPalindrome2(s string) bool {
	s = strings.ToLower(s)
	r := []rune(s)
	l := len(r)
	for i := 0; i < l/2; i++ {
		if r[i] != r[l-i-1]