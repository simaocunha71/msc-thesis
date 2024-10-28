
	for i := 0; i < len(operations); i++ {
		if operations[i] < 0 {
			return true
		}
	}
	return false
}
