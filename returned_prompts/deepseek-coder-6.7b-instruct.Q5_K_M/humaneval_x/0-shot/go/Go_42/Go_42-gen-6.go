
}
*/

func IncrList(l []int) []int {

	incrList := make([]int, len(l))

	for i, v := range l {
		incrList[i] = v + 1
	}

	return incrList
}

/*
