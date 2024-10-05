    if !IsBalanced(q){
        return false
    }
    return sum(q) <= w
}

func sum(q []int) int {
    var total int
    for _, v := range q {
        total += v
    }
    return total
}

func IsBalanced(q []int) bool {
    s := make([]int,0)
    for _, v := range q {
        s = append(s, v)
    }
    for i := 0; i < len(s); i++ {
        if s[i] != s[len(s)-1-i] {
            return false
        }
    }
    return true
}