 
func F(n int) []int {
    f := make([]int, n)
    for i := 1; i < n; i++ {
        if i%2 == 0 {
            f[i] = factorial(i)
        } else {
            f[i] = sum(i)
        }
    }
    return f
}

func factorial(n int) int {
    total := 1
    for i := 1; i <= n; i++ {
        total *= i
    }
    return total
}

func sum(n int) int {
    total := 0
    for i := 1; i <= n; i++ {
        total += i
    }
    return total
}

func main() {
    fmt.Println(F(5))
}

