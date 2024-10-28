	for i := range arr {
		for j := i + 1; j < len(arr); j++ {
			if arr[i] > arr[j] {
				arr[i], arr[j] = arr[j], arr[i]
			}
		}
	}
	return arr
}

func main() {
	arr := []int{1, 5, 2, 3, 4}
	fmt.Println(arr)
	sort.Ints(arr)
	fmt.Println(arr)
	arr = SortArray(arr)
	fmt.Println(arr)
}
