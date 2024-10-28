    result := make([]int, 0)
    for n > 1 {
        for i := 2; i <= n; i++ {
            if n%i == 0 {
                count := 0
                for n%i == 0 {
                    n /= i
                    count++
                }
                result = append(result, int(i))
                for j := 0; j < count; j++ {
                    result = append(result, int(i))
                }
            }
        }
    }
    return result
} 





