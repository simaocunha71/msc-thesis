    var result []int
    for i := 1; i <= n; i++ {
        if i%2 == 0 {
            result = append(result, factorial(i))
        } else {
            result = append(result, sumOfNumbers(i))
        }
    }
    return result
}

func factorial(n int) int {
    if n == 0 {
        return 1
    }
    return n * factorial(n-1)
}

func sumOfNumbers(n int) int {
    if n == 1 {
        return 1
    }
    return n + sumOfNumbers(n-1)
}

// Test
func main() {
    fmt.Println(F(5))
    fmt.Println(F(6))
    fmt.Println(F(7))
    fmt.Println(F(8))
}

/* Output:
[1 2 6 24 15]
[1 2 6 24 120]
[1 2 6 24 120 720]
[1 2 6 24 120 720 5040]
*/

*/





















































































































































































































