	if strings.HasSuffix(txt, " ") {
		return false
	}
	for i := range txt {
		if !(txt[i] >= 'a' && txt[i] <= 'z' || txt[i] >= 'A' && txt[i] <= 'Z') {
			continue A
		}
	}
	return true
}
