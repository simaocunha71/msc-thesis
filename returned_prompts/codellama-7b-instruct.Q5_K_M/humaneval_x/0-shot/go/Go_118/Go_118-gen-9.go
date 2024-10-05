	for i := len(word) - 1; i >= 0; i-- {
		if bytes.IndexByte("aeiou", word[i]) != -1 {
			return word[i : i+1]
		}
	}
	return ""
}

