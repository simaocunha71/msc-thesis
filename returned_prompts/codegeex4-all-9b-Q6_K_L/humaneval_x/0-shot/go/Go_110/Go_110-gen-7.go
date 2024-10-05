func Exchange(lst1, lst2 []int) string {
    evenNums := 0
    oddNums := 0
    for _, num := range lst1 {
        if num%2 == 0 {
            evenNums++
        } else {
            oddNums++
        }
    }
    for _, num := range lst2 {
        if num%2 == 0 {
            evenNums++
        } else {
            oddNums++
        }
    }
    if oddNums <= evenNums {
        return "YES"
    }
    return "NO"
}

func main() {
    fmt.Println(Exchange([]int{1, 2, 3, 4}, []int{1, 2, 3, 4}))
    fmt.Println(Exchange([]int{1, 2, 3, 4}, []int{1, 5, 3, 4}))
}