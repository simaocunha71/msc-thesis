
	res := make([]int, len(l))
	for i, v := range l {
		res[i] = v + 1
	}
	return res
}

func main() {
	l := []int{1, 2, 3}
	fmt.Println(IncrList(l))
	l = []int{5, 3, 5, 2, 3, 3, 9, 0, 123}
	fmt.Println(IncrList(l))
}

*/

// 