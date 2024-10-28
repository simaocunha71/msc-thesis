    var inc bool = false
    var dec bool = false
    for i := 0; i < len(l)-1; i++ {
        if l[i] < l[i+1] {
            inc = true
        } else if l[i] > l[i+1] {
            dec = true
        }
        if inc && dec {
            return false
        }
    }
    return inc || dec
}



