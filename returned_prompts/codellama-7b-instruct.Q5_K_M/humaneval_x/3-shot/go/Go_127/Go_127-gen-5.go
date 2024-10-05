    if num < 2 {
        return false
    }
    if num == 2 {
        return true
    }

    var i int = 2
    for i*i <= num {
        if num % i == 0{
            return false
        }
        i += 1
    }

    return true
}



