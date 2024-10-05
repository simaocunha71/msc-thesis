
	length := len(lst)
	if length == 0 || length == 1 {
		return true
	}

	for i := 1; i < length; i++ {
		if lst[i-1] > lst[i] {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println(IsSorted([]int{5})) // true
	fmt.Println(IsSorted([]int{1, 2, 3, 4, 5})) // true
	fmt.Println(IsSorted([]int{1, 3, 2, 4, 5})) // false
	fmt.Println(IsSorted([]int{1, 2, 3, 4, 5, 6})) // true
	fmt.Println(IsSorted([]int{1, 2, 3, 4, 5, 6, 7})) // true
	fmt.Println(IsSorted([]int{1, 2, 2, 3, 3, 4})) // true
	fmt.Println(IsSorted([]int{1, 2, 2, 2, 3, 4})) // false
}



// This program defines a function IsSorted that checks if a given list of integers is sorted in ascending order. 
// It iterates over the list and compares each pair of adjacent numbers. If it finds a pair where the first number is greater 
// than the second, it returns false, indicating that the list is not sorted. If it doesn't find any such pair, it returns true, 
// indicating that the list is sorted. The main function demonstrates the usage of this function with several examples.
// 
// The function works by iterating over the list and comparing each pair of adjacent numbers. If it finds a pair where the first 
// number is greater than the second, it returns false immediately. If it gets through the entire list without finding such a 
// pair, it returns true. This is because by definition, a list is sorted if and only if it is in ascending order.
// 
// The time complexity of this function is O(n), where n is