    n := len(xs)
    if n%2 != 0 {
        panic("xs must have even number of elements")
    }
    if xs[n/2] == 0 {
        panic("largest coefficient must be nonzero")
    }
    if n == 2 {
        return -xs[0] / xs[1]
    }
    mid := n/2
    if xs[mid] == 0 {
        panic("mid coefficient must be nonzero")
    }
    return FindZero(xs[:mid])
}




