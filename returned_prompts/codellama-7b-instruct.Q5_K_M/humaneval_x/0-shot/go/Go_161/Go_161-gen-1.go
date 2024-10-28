	for i, v := range s {
		if v >= 'a' && v <= 'z' {
			s = s[0:i] + string(v^32) + s[i+1:]
	