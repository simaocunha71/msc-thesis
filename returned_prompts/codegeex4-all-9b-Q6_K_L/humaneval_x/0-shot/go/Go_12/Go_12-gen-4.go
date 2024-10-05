func Longest(strings []string) interface{}{
	if len(strings) == 0 {
		return nil
	}
	longest := strings[0]
	for _, s := range strings {
		if len(s) > len(longest) {
			longest = s
		}
	}
	return longest
}