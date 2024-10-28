    if a<100 {
        return false
    }

    var p = make([]int, 0)
    for i := 2; i < 100; i++ {
        if a % i == 0 {
            p = append(p, i)
            a = a / i

            if a < 100 {
                if len(p) == 3{
                    return true
                }
                return false
            }
        }
    }
    return false
}



