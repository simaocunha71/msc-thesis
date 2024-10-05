func TotalMatch(lst1 []string,lst2 []string) []string {
	if len(lst1) == 0 && len(lst2) == 0 {
		return lst1
	}

	if len(lst1) == 0 {
		return lst2
	}

	if len(lst2) == 0 {
		return lst1
	}

	count1 := 0
	for _, v := range lst1 {
		count1 += len(v)
	}

	count2 := 0
	for _, v := range lst2 {
		count2 += len(v)
	}

	if count1 == count2 {
		return lst1
	}

	if count1 < count2 {
		return lst1
	}

	return lst2
}