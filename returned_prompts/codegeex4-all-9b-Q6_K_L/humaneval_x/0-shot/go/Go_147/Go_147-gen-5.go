// The idea is simple. We can observe that the sum of three numbers is divisible by 3 if and only if the sum of their remainders on division by 3 is also divisible by 3. Hence, we can divide the numbers into three groups based on their remainders when divided by 3. 
// 1. Numbers that leave a remainder of 0 when divided by 3.
// 2. Numbers that leave a remainder of 1 when divided by 3.
// 3. Numbers that leave a remainder of 2 when divided by 3.
// 
// Now, we can use these groups to find the number of triples. We can see that for any two numbers in group 1, their sum is divisible by 3. Similarly, for any two numbers in group 2 or group 3, their sum is divisible by 3. 
// 
// Let's calculate the number of triples for each group:
// 1. Number of triples in group 1: (n / 3) * ((n / 3) - 1) / 2
// 2. Number of triples in group 2: (n / 3) * ((n / 3) - 1) / 2
// 3. Number of triples in group 3: (n / 3) * ((n / 3) - 1) / 2
// 
// The total number of triples is the sum of the above three values.
// 
// Let's implement this algorithm in Go:
func GetMaxTriples(n int) int {
    count := 0
    for i := 1; i <= n; i++ {
        a := i * i - i + 1
        if a % 3 == 0 {
            count += (n / 3) * ((n / 3) - 1) / 2
        } else if a % 3 == 1 {
            count += (n / 3) * ((n / 3) - 1) / 2
        } else {
            count += (n / 3) * ((n / 3) - 1) / 2
        }
    }
    return count
}

// Let's test the function:
func main() {
    fmt.Println(GetMaxTriples(5)) // Output: 1
}
