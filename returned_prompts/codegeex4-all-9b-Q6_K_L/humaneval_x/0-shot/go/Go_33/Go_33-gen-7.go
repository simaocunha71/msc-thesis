```go
func SortThird(l []int) []int {
    var l_prime []int
    l_div_three := []int{}
    for i, num := range l {
        if i % 3 == 0 {
            l_div_three = append(l_div_three, num)
        } else {
            l_prime = append(l_prime, num)
        }
    }
    sort.Ints(l_div_three)
    j := 0
    for i, num := range l {
        if i % 3 == 0 {
            l_prime = append(l_prime, l_div_three[j])
            j++
        }
    }
    return l_prime
}
```
