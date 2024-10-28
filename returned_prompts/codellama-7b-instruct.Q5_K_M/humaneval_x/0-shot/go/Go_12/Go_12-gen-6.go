	// Implemented
	if len(strings) == 0 {
		return nil
	}
	var longest string
	for _, s := range strings {
		if len(s) > len(longest) || (len(s) == len(longest) && longest == "") {
			longest = s
		}
	}
	return longest
}
