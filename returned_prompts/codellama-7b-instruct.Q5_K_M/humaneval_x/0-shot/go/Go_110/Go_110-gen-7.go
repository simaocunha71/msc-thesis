
// If the len of the lists is 0, return "NO".
	if len(lst1) == 0 || len(lst2) == 0 {
		return "NO"
	}

// If the len of the lists is 1, return "NO".
	if len(lst1) == 1 || len(lst2) == 1 {
		return "NO"
	}

// If the len of the lists is 2, return "YES" if the even number is found in the
// list, else "NO".
	if len(lst1) == 2 || len(lst2) == 2 {
		if len(lst1) == 2 && len(lst2) == 2 {
			if findEven(lst1) || findEven(lst2) {
				return "YES"
			}
			return "NO"
		}
		if len(lst1) == 2 {
			if findEven(lst1) {
				return "YES"
			}
			return "NO"
		}
		if len(lst2) == 2 {
			if findEven(lst2) {
				return "YES"
			}
			return "NO"
		}
	}

// If the len of the lists is greater than 2, then the function will be called
// recursively.
	for i := 0; i < len(lst1); i++ {
		for j := 0; j < len(lst2); j++ {
			if lst1[i]%2 == 0 && lst2[j]%2 == 0 {
				if Exchange(lst1[:i], lst2[j:]) == "YES" {
					return "YES"
				}
				if Exchange(lst1[i:], lst2[:j]) == "YES" {
					return "YES"
				}
			}
		}
	}

	return "