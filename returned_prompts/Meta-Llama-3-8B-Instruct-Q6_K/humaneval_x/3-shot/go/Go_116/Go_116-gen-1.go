    type pair struct {
        num int
        ones int
    }

    sort.Slice(arr, func(i, j int) bool {
        p1 := pair{arr[i], 0}
        p2 := pair{arr[j], 0}
        
        for p1.num > 0 {
            p1.num /= 2
            p1.ones += p1.num % 2
        }
        
        for p2.num > 0 {
            p2.num /= 2
            p2.ones += p2.num % 2
        }
        
        if p1.ones != p2.ones {
            return p1.ones < p2.ones
        }
        
        return p1.num < p2.num
    })
    
    return arr
}