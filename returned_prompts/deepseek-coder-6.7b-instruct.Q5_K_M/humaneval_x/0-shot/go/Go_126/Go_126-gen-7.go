
	dup_check := make(map[int]int)
	for i := 0; i < len(lst) - 1; i++ {
		if _, ok := dup_check[lst[i]]; ok {
			return false
		}
		dup_check[lst[i]] = 1
		if lst[i] >= lst[i + 1] {
			return false
		}
	}
	if _, ok := dup_check[lst[len(lst) - 1]]; ok {
		return false
	}

	return true
}

// IsSorted([5]) ➞ true
// IsSorted([1, 2, 3, 4, 5]) ➞ true
// IsSorted([1, 3, 2, 4, 5]) ➞ false
// IsSorted([1, 2, 3, 4, 5, 6]) ➞ true
// IsSorted([1, 2, 3, 4, 5, 6, 7]) ➞ true
// IsSorted([1, 3, 2, 4, 5, 6, 7]) ➞ false
// IsSorted([1, 2, 2, 3, 3, 4]) ➞ true
// IsSorted([1, 2, 2, 2, 3, 4]) ➞ false

