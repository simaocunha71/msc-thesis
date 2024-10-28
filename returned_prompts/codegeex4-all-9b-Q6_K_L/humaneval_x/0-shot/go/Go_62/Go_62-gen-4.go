func Derivative(xs []int) []int {
    l := len(xs)
    if l < 2 {
        return []int{}
    }
    res := make([]int, l-1)
    for i := 1; i < l; i++ {
        res[i-1] = xs[i] * i
    }
    return res
}

func main() {
    fmt.Println(Derivative([]int{3, 1, 2, 4, 5})) // [1, 4, 12, 20]
    fmt.Println(Derivative([]int{1, 2, 3}))       // [2, 6]
}