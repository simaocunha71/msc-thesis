    if len(xs)%2==1||len(xs)==0{
        panic("FindZero: invalid arguments")
    }
    if xs[0]==0{
        panic("FindZero: leading coefficient is 0")
    }
    x0 := -float64(xs[1])/float64(xs[0])
    return x0
}



