
// Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
// >>> Intersperse([], 4)
// []
// >>> Intersperse([1, 2, 3], 4)
// [1, 4, 2, 4, 3]
func Intersperse(numbers []int, delimeter int) []int {
	if len(numbers) == 0 {
		return numbers
	}

	var result []int
	for i := 0; i < len(numbers)-1; i++ {
		result = append(result, numbers[i])
		result = append(result, delimeter)
	}
	result = append(result, numbers[len(numbers)-1])
	return result
}

func main() {
	fmt.Println(Intersperse([]int{}, 4))
	fmt.Println(Intersperse([]int{1, 2, 3}, 4))
	fmt.Println(Intersperse([]int{1, 2, 3, 4, 5, 6}, 4))
}

Output:
[]
[1 4 2 4 3]
[1 4 2 4 3 4 5 4 6]

Expected:
[]
[1 4 2 4 3]
[1 4 2 4 3 4 5 4 6 4]

Note:
- The second example is OK, but I think there's a better solution.

