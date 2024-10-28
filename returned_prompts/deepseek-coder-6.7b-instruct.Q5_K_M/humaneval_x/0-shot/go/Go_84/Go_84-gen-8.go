    // Given a positive integer N, return the total sum of its digits in binary.
    // 
    // Example
    // For N = 1000, the sum of digits will be 1 the output should be "1".
    // For N = 150, the sum of digits will be 6 the output should be "110".
    // For N = 147, the sum of digits will be 12 the output should be "1100".
    // 
    // Variables:
    // @N integer
    // Constraints: 0 ≤ N ≤ 10000.
    // Output:
    // a string of binary number


func Solve(N int) string {
    // Convert integer to string
    strN := strconv.Itoa(N)
    sum := 0

    // Convert each digit to integer and add them up
    for _, digit := range strN {
        digitInt, _ := strconv.Atoi(string(digit))
        sum += digitInt
    }

    // Convert the sum to a binary string
    binStr := strconv.FormatInt(int64(sum), 2)

    return binStr
}

*/

func Solve(N int) string {
	// Convert integer to string
	strN := strconv.Itoa(N)
	sum := 0

	// Convert each digit to integer and add them up
	for _, digit := range strN {
		digitInt, _ := strconv.Atoi(string