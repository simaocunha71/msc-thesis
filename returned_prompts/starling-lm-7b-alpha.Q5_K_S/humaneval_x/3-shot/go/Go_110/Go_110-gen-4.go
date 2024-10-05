    odd_count:= 0
    for _,i := range lst1{
        if i%2==1{
            odd_count += 1
        }
    }
    if odd_count%2==0{
        for _,i := range lst2{
            if i%2==0 && odd_count>0{
                odd_count -= 1
                lst1 = append(lst1[:i], lst1[i+1:]...)
                return "YES"
            }
        }
    }
    return "NO"
}



