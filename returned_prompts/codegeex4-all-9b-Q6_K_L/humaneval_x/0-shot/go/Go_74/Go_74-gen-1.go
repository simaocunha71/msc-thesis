// 1. get the total number of chars in the first list
// 2. get the total number of chars in the second list
// 3. if the first list has less chars, return the first list
// 4. if the second list has less chars, return the second list
// 5. if both lists have the same number of chars, return the first list
// 6. if both lists have the same number of chars, return the second list

func TotalMatch(lst1 []string,lst2 []string) []string {
    var total1, total2 int
    for _, str := range lst1 {
        total1 += len(str)
    }
    for _, str := range lst2 {
        total2 += len(str)
    }
    if total1 < total2 {
        return lst1
    } else if total2 < total1 {
        return lst2
    } else {
        return lst1
    }
}