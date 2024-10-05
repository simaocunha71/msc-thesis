    if len(q) == 1{
        if q[0] <= w{
            return true
        }
        return false
    }

    if q[0] == q[len(q)-1]{
        var sum int = 0
        for _, i := range q{
            sum += i
        }
        if sum > w{
            return false
        }
        return true
    }
    return false
}



