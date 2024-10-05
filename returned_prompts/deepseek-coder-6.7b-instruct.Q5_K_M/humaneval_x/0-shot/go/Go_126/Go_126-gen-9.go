
	n := len(lst)
	if n <= 1 {
		return true
	}

	for i := 1; i < n; i++ {
		if lst[i] < lst[i-1] {
			return false
		}
	}

	return true
}

func main() {

	fmt.Println(IsSorted([]int{5})) // ➞ true
	fmt.Println(IsSorted([]int{1, 2, 3, 4, 5})) // ➞ true
	fmt.Println(IsSorted([]int{1, 3, 2, 4, 5})) // ➞ false
	fmt.Println(IsSorted([]int{1, 2, 3, 4, 5, 6})) // ➞ true
	fmt.Println(IsSorted([]int{1, 2, 3, 4, 5, 6, 7})) // ➞ true
	fmt.Println(IsSorted([]int{1, 3, 2, 4, 5, 6, 7})) // ➞ false
	fmt.Println(IsSorted([]int{1, 2, 2, 3, 3, 4})) // ➞ true
	fmt.Println(IsSorted([]int{1, 2, 2, 2, 3, 4})) // ➞ false
}
*/

// Given a list of numbers, return whether or not they are sorted
// in ascending order. If list has more than 1 duplicate of the same
// number, return false. Assume no negative numbers and only integers.
// 
// Examples
// IsSorted([5]) ➞ true
// IsSorted([1, 2, 3, 4, 5]) ➞ true
// IsSorted([1, 3, 2, 4, 5]) ➞ false
// IsSorted([1, 2, 3, 4, 5, 6]) ➞ true
// IsSorted