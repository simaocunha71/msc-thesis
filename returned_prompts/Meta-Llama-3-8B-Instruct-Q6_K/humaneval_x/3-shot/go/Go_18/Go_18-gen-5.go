    count := 0
    for i := 0; i <= len(str); i++ {
        j := 0
        for j < len(substring) {
            if i+j >= len(str) {
                break
            }
            if str[i+j] != substring[j] {
                break
            }
            j++
        }
        if j == len(substring) {
            count++
            i += j - 1
        }
    }
    return count
}