	sort.Ints(l)
	return l
}

B:
func SortEven(l []int) []int {
	for i := 1; i < len(l); i += 2 {
		sort.Ints(l[i:])
	}
	return l
}

C:
func SortEven(l []int) []int {
	for i := 0; i < len(l); i += 2 {
		sort.Ints(l[i:])
	}
	return l
}

D:
func SortEven(l []int) []int {
	sort.Slice(l, func(i, j int) bool { return l[i] < l[j] })
	return l
}
