
	// If l has only one element, it cannot be a triples sum to zero.
	if len(l) == 1 {
		return false
	}

	// If l has two elements, it cannot be a triples sum to zero.
	if len(l) == 2 {
		return false
	}

	// If l has three elements, it cannot be a triples sum to zero.
	if len(l) == 3 {
		return false
	}

	// If l has four or more elements, it can be a triples sum to zero.
	if len(l) >= 4 {
		for i := 0; i < len(l); i++ {
			for j := i + 1; j < len(l); j++ {
				for k := j + 1; k < len(l); k++ {
					if l[i] + l[j] + l[k] == 0 {
						return true
					}
				}
			}
		}
	}

	return false
}

func main() {
	fmt.Println(TriplesSumToZero([]int{1, 3, 5, 0}))
	fmt.Println(TriplesSumToZero([]int{1, 3, -2, 1}))
	fmt.Println(TriplesSumToZero([]int{1, 2, 3, 7}))
	fmt.Println(TriplesSumToZero([]int{2, 4, -5, 3, 9, 7}))
	fmt.Println(TriplesSumToZero([]int{1}))
}
