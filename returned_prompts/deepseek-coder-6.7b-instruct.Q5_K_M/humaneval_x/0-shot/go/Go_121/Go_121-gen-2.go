
    sum := 0
    for i := 0; i < len(lst); i += 2 {
        if lst[i] % 2 != 0 {
            sum += lst[i]
        }
    }
    return sum
}

func main() {
    fmt.Println(Solution([]int{5, 8, 7, 1})) // 12
    fmt.Println(Solution([]int{3, 3, 3, 3, 3})) // 9
    fmt.Println(Solution([]int{30, 13, 24, 321})) // 0
}

*/

// 解答

func Solution(lst []int) int {
	sum := 0
	for i := 0; i < len(lst); i += 2 {
		if lst[i]%2 != 0 {
			sum += lst[i]
		}
	}
	return sum
}

func main() {
	fmt.Println(Solution([]int{5, 8, 7, 1}))                // 12
	fmt.Println(Solution([]int{3, 3, 3, 3, 3}))             // 9
	fmt.Println(Solution([]int{30, 13, 24, 321}))            // 0
	fmt.Println(Solution([]int{23, 45, 67, 234, 456, 789})) // 789
}

// この問題の考え方はシンプルだった。偶数位置の要素をチェックし、それが奇数であるかどうかをチェックする。
// それが奇数である場合は、その要素を sum に加算する