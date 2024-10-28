    sort.Slice(l, func(i, j int) bool {
        return l[i] < l[j]
    })

    l_len := len(l)
    if l_len % 2 == 0 {
        return float64(l[l_len/2 - 1] + l[l_len/2])/2
    }else{
        return float64(l[l_len/2])
    }
}



