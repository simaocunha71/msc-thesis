func Add(lst []int) int {
    return 0
}

func Add(lst []int) int {
    var sum int
    for i := 0; i < len(lst); i++ {
        if i%2 == 0 && lst[i]%2 == 0 {
            sum += lst[i]
        }
    }
    return sum
}