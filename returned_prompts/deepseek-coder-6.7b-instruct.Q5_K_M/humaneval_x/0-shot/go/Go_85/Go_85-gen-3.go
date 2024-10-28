
    sum := 0
    for i, v := range lst {
        if i % 2 != 0 && v % 2 == 0 {
            sum += v
        }
    }
    return sum
}

func main() {
    fmt.Println(Add([]int{4, 2, 6, 7})) // 2
    fmt.Println(Add([]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10})) // 14
    fmt.Println(Add([]int{10, 20, 30, 40, 50, 60})) // 140
}

*/

/*
