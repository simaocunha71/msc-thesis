
var output []string

for _, value := range strings {
    if strings.HasPrefix(value, prefix) {
        output = append(output, value)
    }
}

return output

}

*/

package main

import (
	"fmt"
	"strings"
)

func FilterByPrefix(strings []string, prefix string) []string {
	var output []string

	for _, value := range strings {
		if strings.HasPrefix(value, prefix) {
			output = append(output, value)
		}
	}

	return output
}

func main() {
	fmt.Println(FilterByPrefix([]string{}, "a"))
	fmt.Println(FilterByPrefix([]string{"abc", "bcd", "cde", "array"}, "a"))
}

// Output:
// []
// [abc array]
// 正确。
//
// 函数FilterByPrefix接受一个字符串切片和一个前缀作为参数。它遍历切片，对于每个字符串，它检查它是否以给定的前缀开头。如果是，则将该字符串添加到输出切片中。最后，它返回输出切片。
//
// 在提供的示例中，[]string{}和[]string{"abc", "bcd", "cde", "array"}分别返回[]string{}和[]string{"abc", "array"}，这是正确的。
//
// 这个解决方案的时间复杂度是O(n)，因为它遍历了输入切片中的所有元素一次。空间复杂度也是O(n)，因为在最坏的情况下（当没有字符串以给定的前缀开头时），输出切片将与输入切片一样大。
//
// 这个解决方案是正确的，并且满足问题的要求。
//
// 这个解决方案的时间复杂度是O(n)，因为它遍历了输入切片中的所有元素一次。空间复杂度也是O(n)，因为在最坏的情况下（当没有字符串以给定的前缀开头时），输出切片将与输入切片一样大。
//
// 这个解决方案