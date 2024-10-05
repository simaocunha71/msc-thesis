    for _, num := range lst1 {
        if num%2 != 0 {
            for _, num2 := range lst2 {
                if num2%2 == 0 {
                    lst1 = removeElement(lst1, num)
                    lst2 = append(lst2, num)
                    return "YES"
                }
            }
        }
    }
    return "NO"
}

func removeElement(nums []int, val int) []int {
    result := make([]int, 0)
    for _, num := range nums {
        if num != val {
            result = append(result, num)
        }
    }
    return result
}