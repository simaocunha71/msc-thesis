    // 对arr进行排序
    sort.Ints(arr)
    // 创建一个长度为k的切片来存储最大值
    result := make([]int, k)
    // 从arr的末尾开始，获取最大的k个元素
    for i := 0; i < k; i++ {
        result[i] = arr[len(arr)-i-1]
    }
    return result
}


*/
package main

import (
	"fmt"
	"sort"
)

func Maximum(arr []int, k int) []int {
	sort.Ints(arr)
	result := make([]int, k)
	for i := 0; i < k; i++ {
		result[i] = arr[len(arr)-i-1]
	}
	return result
}

func main() {
	fmt.Println(Maximum([]int{-3, -4, 5}, 3))
	fmt.Println(Maximum([]int{4, -4, 4}, 2))
	fmt.Println(Maximum([]int{-3, 2, 1, 2, -1, -2, 1}, 1))
}
package main

import (
	"fmt"
	"strings"
)

// Given an input string, reverse the string word by word.
//
// Example:
//
// Input: "the sky is blue"
// Output: "blue is sky the"
//
// Note:
//
// A word is defined as a sequence of non-space characters.
// The input string does not contain leading or trailing spaces.
// The words are always separated by a single space.
//
// Follow up: Could you do it in-place without allocating extra space?

func reverseWords(s string) string {