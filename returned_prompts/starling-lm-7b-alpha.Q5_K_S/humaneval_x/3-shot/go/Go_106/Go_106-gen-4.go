    result := make([]int, n)
    for i:=1;i<=n;i++{
        if i%2==0{
            result[i-1]=i
        }else{
            result[i-1]=sum_i(i)
        }
    }
    return result
}

func sum_i(i int) int{
    if i==1{
        return 1
    }
    return i+sum_i(i-1)
}





