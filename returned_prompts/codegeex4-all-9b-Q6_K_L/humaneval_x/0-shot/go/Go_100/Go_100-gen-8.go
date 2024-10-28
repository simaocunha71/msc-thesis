func MakeAPile(n int) []int {
    if n == 0 {
        return []int{}
    }

    if n == 1 {
        return []int{1}
    }

    if n % 2 == 0 {
        return append(MakeAPile(n - 1), n + 1)
    }

    return append(MakeAPile(n - 1), n + 2)
}