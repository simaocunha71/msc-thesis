	odd := []int{}
	for i := 1; i < len(l); i += 2 {
		odd = append(odd, l[i])
	}
	sort.Ints(odd)

	res := []int{}
	for i, j := 0, 0; i < len(l); i++ {
		if i%2 == 0 {
			res = append(res, l[i])
		} else {
			res = append(res, odd[j])
			j++
		}
	}
	return res
}

// This function takes a list l and returns a list l' such that
// l' is a rearrangement of l, where each value in l' is equal to the average of its neighbors in l.
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
