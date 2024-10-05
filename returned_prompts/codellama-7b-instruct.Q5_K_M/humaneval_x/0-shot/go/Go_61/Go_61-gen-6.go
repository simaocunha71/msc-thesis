for _, char := range brackets {
	if char == '(' {
		// found an opening bracket
		continue
	}
	if char == ')' {
		// found a closing bracket
		return true
	}
}

return false
}
