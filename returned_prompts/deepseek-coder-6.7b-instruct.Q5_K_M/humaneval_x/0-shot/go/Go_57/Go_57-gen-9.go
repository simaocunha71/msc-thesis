
	increasing := true
	decreasing := true
	for i := 0; i < len(l)-1; i++ {
		if l[i] > l[i+1] {
			increasing = false
		}
		if l[i] < l[i+1] {
			decreasing = false
		}
	}
	
	if increasing {
		return true
	}
	if decreasing {
		return true
	}
	return false
}

// Main function
func main() {

B:

	fmt.Println(Monotonic([]int{1, 2, 4, 20})) // true
	fmt.Println(Monotonic([]int{1, 20, 4, 10})) // false
	fmt.Println(Monotonic([]int{4, 1, 0, -10})) // true
}

// Output:
// true
// false
// true


// Output for test cases:
// true
// false
// true
*/

// Return true if the list of integers is monotonically increasing or decreasing.
func Monotonic(l []int) bool {
	increasing := true
	decreasing := true
	for i := 0; i < len(l)-1; i++ {
		if l[i] > l[i+1] {
			increasing = false
		}
		if l[i] < l[i+1] {
			decreasing = false
		}
	}
	return increasing || decreasing
}

func main() {
	fmt.Println(Monotonic([]int{1, 2, 4, 20})) // true
	fmt.Println(Monotonic([]int{1, 20, 4, 10})) // false
	fmt.Println(Monotonic([]int{4, 1, 0, -10})) // true
}

// Output:
// true
// false
// true

// Output for test cases:
// true
// false
// true

// Monotonic function returns true if the list of integers is mon