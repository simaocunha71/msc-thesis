func MakeAPile(n int) []int {
    s := make([]int, n)
    for i := 0; i < n; i++ {
        s[i] = 2 * (i + 1)
    }
    return s
}

func MakeAPile(n int) []int {
    s := make([]int, n)
    s[0] = n
    for i := 1; i < n; i++ {
        s[i] = s[i-1] + 2*(i%2+1)
    }
    return s
}

func MakeAPile(n int) []int {
    s := make([]int, n)
    s[0] = n
    for i := 1; i < n; i++ {
        s[i] = s[i-1] + 2*(i%2+1)
    }
    return s
}