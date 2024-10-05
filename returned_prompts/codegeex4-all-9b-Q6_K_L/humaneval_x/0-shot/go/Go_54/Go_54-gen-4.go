func SameChars(s0 string, s1 string) bool {
	return strings.Count(s0, "") == strings.Count(s1, "")
}

func SameChars(s0 string, s1 string) bool {
	return len(s0) == len(s1)
}

func SameChars(s0 string, s1 string) bool {
	return len(s0) == len(s1) && strings.Count(s0, "") == strings.Count(s1, "")
}

func SameChars(s0 string, s1 string) bool {
	return len(s0) == len(s1) && len(s0) == len(set(s0)) && len(s1) == len(set(s1))
}