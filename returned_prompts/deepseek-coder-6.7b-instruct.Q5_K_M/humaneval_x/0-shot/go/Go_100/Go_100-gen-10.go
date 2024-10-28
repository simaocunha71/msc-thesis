
	arr := make([]int, n)

	for i := range arr {
		if n%2 == 0 {
			arr[i] = n + 2*i
		} else {
			arr[i] = n + 2*i
		}
	}
	return arr
}


func main() {

	fmt.Println(MakeAPile(3))

}


//Output:
//[3 5 7]
// Explanation:
// At the start, there are 3 stones.
// The next level has 5 stones (3+2),
// the next level has 7 stones (5+2).
// So we return [3, 5, 7].

//Examples:
//>>> MakeAPile(4)
//[4, 6, 8, 10]
//>>> MakeAPile(5)
//[5, 7, 9, 11, 13]

//Output:
//[4, 6, 8, 10]
//[5, 7, 9, 11, 13]
//Explanation:
//At the start, there are 4 stones.
//The next level has 6 stones (4+2),
//the next level has 8 stones (6+2),
//the next level has 10 stones (8+2).
//So we return [4, 6, 8, 10].
//Similarly, for n=5, the first level has 5 stones,
//the next level has 7 stones (5+2),
//the next level has 9 stones (7+2),
//the next level has 11 stones (9+2),
//the next level has 13 stones (11+2).
//So we return [5, 7, 9, 11, 13].

//Examples:
//>>> MakeAPile(1)
//[1]

//Output:
//[1]
//Explanation:
//At the start, there is 1 stone.
//So we return [1].

//Examples:
//>>> MakeAPile