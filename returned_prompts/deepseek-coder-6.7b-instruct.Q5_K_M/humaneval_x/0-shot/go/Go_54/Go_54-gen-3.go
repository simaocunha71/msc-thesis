
// 对字符串进行排序
sort.Slice([]rune(s0), func(i, j int) bool { return []rune(s0)[i] < []rune(s0)[j] })
sort.Slice([]rune(s1), func(i, j int) bool { return []rune(s1)[i] < []rune(s1)[j] })

B:

// 比较排序后的字符串
return s0 == s1

}

func main() {

fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddeddabc")) // true
fmt.Println(SameChars("abcd", "dddddddabc")) // true
fmt.Println(SameChars("dddddddabc", "abcd")) // true
fmt.Println(SameChars("eabcd", "dddddddabc")) // false