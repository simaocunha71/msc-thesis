
    count := 0
    for i := 0; i <= len(str) - len(substring); i++ {
        if str[i:i+len(substring)] == substring {
            count++
        }
    }
    return count
}

*/

import "strings"

func HowManyTimes(str string, substring string) int {
	count := strings.Count(str, substring)
	return count
}

func main() {
	fmt.Println(HowManyTimes("", "a"))
	fmt.Println(HowManyTimes("aaa", "a"))
	fmt.Println(HowManyTimes("aaaa", "aa"))
}

// 在Go中，使用strings.Count函数可以更简洁地实现相同的功能。
// 它会自动处理重叠的情况，并且不需要手动实现循环来检查每个可能的子字符串。
// 它会计算给定字符串中子字符串出现的次数，并返回计数值。
// 在这种情况下，它相当于在循环中检查每个子字符串，并在找到匹配时递增计数。
// 如果给定字符串或子字符串为空，它将返回0。
// 这个函数的复杂度是O(n)，其中n是给定字符串的长度。
// 这是因为strings.Count函数需要扫描整个字符串来计算出现次数。
// 如果字符串或子字符串非常大，这种方法可能效率低下，但对于正常使用的字符串来说，它是高效的。
// 如果您需要处理非常大的字符串，可以考虑使用不同的算法或数据结构。
// 例如，如果您需要处理非常大的字符串，可以考虑使用后缀树或KMP算法来高效地搜索子字符串。
