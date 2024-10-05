
	if len(s0) == len(s1) {
		for i := 0; i < len(s0); i++ {
			if s0[i] != s1[i] {
				return false
			}
		}
		return true
	}
	return false
}

func main() {
	fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddeddabc"))
	fmt.Println(SameChars("abcd", "dddddddabc"))
	fmt.Println(SameChars("dddddddabc", "abcd"))
	fmt.Println(SameChars("eabcd", "dddddddabc"))
	fmt.Println(SameChars("abcd", "dddddddabce"))
	fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddddabc"))
}
