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
    a := make([]int, n)
    for i := 0; i < n; i++ {
        a[i] = i*i - i + 1
    }

    count := 0
    for i := 0; i < n; i++ {
        for j := i+1; j < n; j++ {
            for k := j+1; k < n; k++ {
                if (a[i] + a[j] + a[k]) % 3 == 0 {
                    count++
                }
            }
        }
    }

    return count
}

func main() {
    fmt.Println(GetMaxTriples(5)) // Output: 1
}

func GetMaxTriples(n int) int {
    a := make([]int, n)
    for i := 0; i < n; i++ {
        a[i] = i*i - i + 1
    }

    count := 0
    for i := 0; i < n; i++ {
        for j := i+1; j < n; j++ {
            for k := j+1; k < n; k++ {
                if (a[i] + a[j] + a[k]) % 3 == 0 {
                    count++
                }
            }
        }
    }

    return count
}

func main() {
    fmt.Println(GetMaxTriples(5)) // Output: 1
}

func GetMaxTriples(n int) int {
    a := make([]int, n)
    for i := 0; i < n; i++ {
        a[i] = i*i - i + 1
    }

    count := 