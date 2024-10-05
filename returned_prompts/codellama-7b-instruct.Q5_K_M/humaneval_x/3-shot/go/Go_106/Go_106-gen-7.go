    result := make([]int, n)
    for i:=1; i<n; i++{
        if i%2==0{
            result[i] = i
        }else{
            result[i] = i*1+i*2+i*3+i*4+i*5
        }
    }
    return result
}


