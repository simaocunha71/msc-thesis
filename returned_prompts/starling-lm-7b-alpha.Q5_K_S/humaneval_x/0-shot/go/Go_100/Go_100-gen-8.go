
func MakeAPile(n int) []int {
    pile := make([]int, n)
    pile[0] = n

    for i := 1; i < n; i++ {
        if n%2 == 0 {
            pile[i] = pile[i-1] + 2
        } else {
            pile[i] = pile[i-1] + 1
        }
    }
    return pile
}


func MakeAPile(n int) []int {
    pile := make([]int, n)
    pile[0] = n

    for i := 1; i < n; i++ {
        if i%2 == 0 {
            pile[i] = pile[i-1] + 1
        } else {
            pile[i] = pile[i-1] + 2
        }
    }
    return pile
}


func MakeAPile(n int) []int {
    pile := make([]int, n)
    pile[0] = n

    for i := 1; i < n; i++ {
        if n%2 == 0 {
            pile[i] = pile[i-1] + 2
        } else {
            pile[i] = pile[i-1] + 1
        }
    }
    return pile
}


func MakeAPile(n int) []int {
    pile := make([]int, n)
    pile[0] = n

    for i := 1; i < n; i++ {
        if i%2 == 0 {
            pile[i] = pile[i-1] + 2
        } else {
            pile[i] = pile[i-1] + 1
        }
    }
    return pile
}


func MakeAPile(n int) []int {
    pile := make([]int, n)
    pile[0] = n

    for i := 1; i < n; i++ {
        if i%2 == 0 {
            pile[i] = pile[i-1] + 1
        } else {
            pile[i] =