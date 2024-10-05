// You are given a positive integer n. You have to create an integer array a of length n.
// For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
// Return the number of triples (a[i], a[j], a[k]) of a where i < j < k,
// and a[i] + a[j] + a[k] is a multiple of 3.
// 
// Example :
// Input: n = 5
// Output: 1
// Explanation:
// a = [1, 3, 7, 13, 21]
// The only valid triple is (1, 7, 13).
func GetMaxTriples(n int) int {

    // Initialize the array a with values i * i - i + 1 for each i from 1 to n
    a := make([]int, n)
    for i := 1; i <= n; i++ {
        a[i-1] = i*i - i + 1
    }

    // Initialize a counter to keep track of the number of valid triples
    count := 0

    // Iterate over all possible triples (i, j, k) where i < j < k
    for i := 0; i < n-2; i++ {
        for j := i+1; j < n-1; j++ {
            for k := j+1; k < n; k++ {
                // Check if the sum of a[i], a[j], and a[k] is a multiple of 3
                if (a[i] + a[j] + a[k]) % 3 == 0 {
                    // If it is, increment the counter
                    count++
                }
            }
        }
    }

    // Return the final count of valid triples
    return count
}

func main() {
    fmt.Println(GetMaxTriples(5)) // Output: 1
}


func GetMaxTriples(n int) int {

    // Initialize the array a with values i * i - i + 1 for each i from 1 to n
    a := make([]int, n)
    for i := 1; i <= n; i++ {
        a[i-1] = i*i - i + 1
    }

    // Initialize a counter to keep track of the number of valid triples
    count := 0

   