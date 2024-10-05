    sort.Slice(arr, func(i, j int) bool {
        bi, bj := fmt.Sprintf("%b", arr[i]), fmt.Sprintf("%b", arr[j])
        cnti, cntj := 0, 0
        for _, v := range bi {
            if v == '1' {
                cnti++
            }
        }
        for _, v := range bj {
            if v == '1' {
                cntj++
            }
        }
        if cnti == cntj {
            return arr[i] < arr[j]
        }
        return cnti < cntj
    })
    return arr
}



