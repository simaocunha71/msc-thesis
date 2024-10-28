    var result [2]int
    for i := 1; i <= n; i++ {
        if IsPalindrome(i) {
            if IsEven(i) {
                result[0] += 1
            } else {
                result[1] += 1
            }
        }
    }
    return result
}



