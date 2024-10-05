	sorted := make([]int, len(l))
	copy(sorted, l)
	sort.Slice(sorted[0:], func(i, j int) bool {
		return i%2 < j%2
	})
	return sorted


	// EvenIndices := make([]int, 0)
	// for i := 0; i < len(l); i += 2 {
	// 	EvenIndices = append(EvenIndices, i)
	// }
	// odds := make([]int, 0)
	// for i := 1; i < len(l); i += 2 {
	// 	odds = append(odds, i)
	// }
	// oddSorted := make([]int, len(odds))
	// copy(oddSorted, l[odds...])
	// sort.Slice(oddSorted, func(i, j int) bool {
	// 	return l[oddSorted[i]] < l[oddSorted[j]]
	// })
	// evenSorted := make([]int, len(EvenIndices))
	// copy(evenSorted, l[EvenIndices...])
	// sort.Slice(evenSorted, func(i, j int) bool {
	// 	return l[evenSorted[i]] < l[evenSorted[j]]
	// })
	// result := make([]int, 0)
	// for i := 0; i < len(l); i++ {
	// 	if i%2 == 0 {
	// 		result = append(result, l[i])
	// 	} else {
	// 		result = append(result, oddSorted[i/2])
	// 	}
	// }
	// return result
}






















































































