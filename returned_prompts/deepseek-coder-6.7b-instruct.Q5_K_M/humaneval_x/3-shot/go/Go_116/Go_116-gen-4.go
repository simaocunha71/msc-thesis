    sort.Slice(arr, func(i, j int) bool {
        iBin, jBin := fmt.Sprintf("%b", arr[i]), fmt.Sprintf("%b", arr[j])
        iOnes, jOnes := 0, 0
        for _, v := range iBin {
            if v == '1' {
                iOnes++
            }
        }
        for _, v := range jBin {
            if v == '1' {
                jOnes++
            }
        }
        if iOnes == jOnes {
            return arr[i] < arr[j]
        }
        return iOnes < jOnes
    })
    return arr
}



