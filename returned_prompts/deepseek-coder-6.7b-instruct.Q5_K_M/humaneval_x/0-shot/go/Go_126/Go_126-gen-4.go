
// Check for ascending order
for i := 0; i < len(lst) - 1; i++ {
    if lst[i] >= lst[i + 1] {
        return false
    }
}

return true

}

*/

func IsSorted(lst []int) bool {
	for i := 0; i < len(lst)-1; i++ {
		if lst[i] >= lst[i+1] {
			return false
		}
	}
	return true
}

// Tests

func main() {

	fmt.Println(IsSorted([]int{5})) // true
	fmt.Println(IsSorted([]int{1, 2, 3, 4, 5})) // true
	fmt.Println(IsSorted([]int{1, 3, 2, 4, 5})) // false
	fmt.Println(IsSorted([]int{1, 2, 3, 4, 5, 6})) // true
	fmt.Println(IsSorted([]int{1, 2, 3, 4, 5, 6, 7})) // true
	fmt.Println(IsSorted([]int{1, 3, 2, 4, 5, 6, 7})) // false
	fmt.Println(IsSorted([]int{1, 2, 2, 3, 3, 4})) // true
	fmt.Println(IsSorted([]int{1, 2, 2, 2, 3, 4})) // false
}

// Output:
// true
// true
// false
// true
// true
// false
// true
// false
// true
// false
// true
// true
// false
// true
// false
// true
// false
// true
// false
// true
// false
// true
// false
// true
// false
// true
// false
// true
// false
// true
// false
// true
// false
// true
// false
// true
// false
// true
//