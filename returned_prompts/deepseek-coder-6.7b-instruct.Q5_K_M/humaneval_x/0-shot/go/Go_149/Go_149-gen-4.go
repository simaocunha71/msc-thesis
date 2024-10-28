    sort.Slice(lst, func(i, j int) bool {
        return len(lst[i]) < len(lst[j])
    })

    var result []string

    for i := 0; i < len(lst); i++ {
        if len(lst[i])%2 == 0 {
            result = append(result, lst[i])
        }
    }

    return result
}

// Write a function that accepts a list of numbers as a parameter,
// deletes the numbers that have odd lengths from it,
// and returns the resulted list with a sorted order,
// The list is always a list of integers and never an array of numbers,
// and it may contain duplicates.
// The order of the list should be ascending by length of each number, and you
// should return the list sorted by that rule.
// If two numbers have the same length, sort the list alphabetically.
// The function should return a list of numbers in sorted order.
// You may assume that all numbers will have the same length.
// For example:
// assert list_sort(["11", "1", "111"]) → ["11"]
// assert list_sort(["12", "1", "111", "22"]) → ["12", "22"]
func SortedListSum(lst []string) []string {

    var intLst []int

    for _, str := range lst {
        num, _ := strconv.Atoi(str)
        intLst = append(intLst, num)
    }

    sort.Slice(intLst, func(i, j int) bool {
        return len(strconv.Itoa(intLst[i])) < len(strconv.Itoa(intLst[j]))
    })

    var result []string

    for _, num := range intLst {
        if len(strconv.Itoa(num))%2 == 0 {
            result = append(result, strconv.Itoa(num))
        }
    }

    return result
}


