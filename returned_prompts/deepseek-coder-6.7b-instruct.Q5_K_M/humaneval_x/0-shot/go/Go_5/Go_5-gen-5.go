
	result := []int{}
	for i, n := range numbers {
		result = append(result, n)
		if i < len(numbers)-1 {
			result = append(result, delimeter)
		}
	}
	return result
}

func main() {
	fmt.Println(Intersperse([]int{}, 4))       // []
	fmt.Println(Intersperse([]int{1, 2, 3}, 4)) // [1, 4, 2, 4, 3]
}
*/

// Insert a number 'delimeter' between every two consecutive elements of input list 'numbers'
func Intersperse(numbers []int, delimeter int) []int {
	result := make([]int, 0, len(numbers)*2-1)
	for i, n := range numbers {
		result = append(result, n)
		if i < len(numbers)-1 {
			result = append(result, delimeter)
		}
	}
	return result
}

func main() {
	fmt.Println(Intersperse([]int{}, 4))       // []
	fmt.Println(Intersperse([]int{1, 2, 3}, 4)) // [1, 4, 2, 4, 3]
}

// Intersperse([], 4)
// []

// Intersperse([1, 2, 3], 4)
// [1, 4, 2, 4, 3]
// func main() {
// 	fmt.Println(Intersperse([]int{}, 4))       // []
// 	fmt.Println(Intersperse([]int{1, 2, 3}, 4)) // [1, 4, 2, 4, 3]
// }

// Intersperse([], 4)
// []

// Intersperse([1, 2, 3], 4)
// [1, 4, 2, 4, 3]
// func main()