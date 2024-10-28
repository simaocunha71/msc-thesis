    sum := 0
    for _, element := range q {
        sum += element
    }

    if sum > w {
        return false
    }

    for i := 0; i < len(q)/2; i++ {
        if q[i] != q[len(q)-1-i] {
            return false
        }
    }

    return true
}



