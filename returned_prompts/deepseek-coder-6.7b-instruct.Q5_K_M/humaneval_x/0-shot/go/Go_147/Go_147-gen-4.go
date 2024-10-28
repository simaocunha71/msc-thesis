
    // Your code here

}

*/

func GetMaxTriples(n int) int {

	A := make([]int, n)
	remainders := make([]int, 3)

	for i := 1; i <= n; i++ {
		val := (i * i) - i + 1
		A[i-1] = val
		remainders[val%3]++
	}

	res := (remainders[0]*(remainders[0]-1))/(2)*(remainders[0]-2)/3 +
		remainders[1]*remainders[2] +
		(remainders[1]*(remainders[1]-1))/2*(remainders[1]-2)/3 +
		(remainders[2]*(remainders[2]-1))/2*(remainders[2]-2)/3

	for i := 1; i < n-1; i++ {
		remainders[0], remainders[1], remainders[2] = remainders[0], remainders[1], remainders[2]
		for j := i + 1; j < n; j++ {
			remainders[A[i]%3]--
			remainders[A[j]%3]++
			res += remainders[0] + remainders[1]*remainders[2]
		}
	}

	return res
}

func main() {
	fmt.Println(GetMaxTriples(5))
}






































































































































