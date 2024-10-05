    var pos_nums []int
    for _, num := range l {
        if num > 0 {
            pos_nums = append(pos_nums, num)
        }
    }
    return pos_nums
}



