
	positive := []int{}
	for _, num := range l {
		if num > 0 {
			positive = append(positive, num)
		}
	}
	return positive
}

func main() {
	fmt.Println(GetPositive([]int{-1, 2, -4, 5, 6}))
	fmt.Println(GetPositive([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}))
}


// 