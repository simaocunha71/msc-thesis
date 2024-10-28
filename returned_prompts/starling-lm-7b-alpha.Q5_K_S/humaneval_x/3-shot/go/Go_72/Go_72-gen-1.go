    n := len(q)
    left := 0
    right := n-1
    sum := 0
    for i:=0;i<n/2;i++{
        if q[left]!=q[right]{
            return false
        }
        sum += q[left] + q[right]
        left++
        right--
    }
    return sum<=w && n%2==0
}



