    result := make([]int,0)
    for i:=0;i<len(lst);i++{
        if i%3==0{
            result = append(result, lst[i]*lst[i])
        }else if i%4==0 && i%3!=0{
            result = append(result, lst[i]*lst[i]*lst[i])
        }else{
            result = append(result, lst[i])
        }
    }
    return sum(result)
}

func sum(nums []int) int{
    var result := 0
    for _, n := range nums{
        result += n
    }
    return result
}



