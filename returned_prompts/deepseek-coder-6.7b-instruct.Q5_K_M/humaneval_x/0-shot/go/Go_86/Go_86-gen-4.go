    split := strings.Split(s, " ")
    for i, v := range split {
        char := []rune(v)
        sort.Slice(char, func(i, j int) bool {
            return char[i] < char[j]
        })
        split[i] = string(char)
    }
    return strings.Join(split, " ")
}

*/

func AntiShuffle(s string) string {
	split := strings.Split(s, " ")
	for i, v := range split {
		char := []rune(v)
		sort.Slice(char, func(i, j int) bool {
			return char[i] < char[j]
		})
		split[i] = string(char)
	}
	return strings.Join(split, " ")
}

/*
