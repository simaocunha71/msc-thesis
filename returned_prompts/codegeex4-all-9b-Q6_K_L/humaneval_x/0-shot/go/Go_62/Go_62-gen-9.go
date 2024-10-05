func Derivative(xs []int) []int {
    if len(xs) == 1 {
        return xs
    }
    return xs[1:]
}