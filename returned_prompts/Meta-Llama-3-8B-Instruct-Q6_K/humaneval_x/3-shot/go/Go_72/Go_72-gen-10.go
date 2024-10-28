    if !isBalanced(q){
        return false
    }
    if sum(q) > w{
        return false
    }
    return true

}

func isBalanced(q []int) bool {
    for i := 0; i < len(q); i++ {
        if q[i] != q[len(q)-1-i] {
            return false
        }
    }
    return true
}

func sum(q []int) int {
    total := 0
    for _, v := range q {
        total += v
    }
    return total
}