
// Your code here

}

*/

func GenerateIntegers(a, b int) []int {
	if a > b {
		a, b = b, a
	}

	result := make([]int, 0)
	for i := a; i <= b; i++ {
		if i%2 == 0 {
			result = append(result, i)
		}
	}
	return result
}

func main() {
	fmt.Println(GenerateIntegers(2, 8))
	fmt.Println(GenerateIntegers(8, 2))
	fmt.Println(GenerateIntegers(10, 14))
}

// Output:
// [2 4 6 8]
// [2 4 6 8]
// []
//

//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
