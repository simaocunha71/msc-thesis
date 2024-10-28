func Exchange(lst1, lst2 []int) string {
    // Count the number of odd elements in lst1 and lst2
    oddCount1 := 0
    oddCount2 := 0
    for _, num := range lst1 {
        if num%2 != 0 {
            oddCount1++
        }
    }
    for _, num := range lst2 {
        if num%2 != 0 {
            oddCount2++
        }
    }
    // If lst1 has more odd elements than lst2, return "NO"
    if oddCount1 > oddCount2 {
        return "NO"
    }
    // If lst1 and lst2 have the same number of odd elements, return "YES"
    if oddCount1 == oddCount2 {
        return "YES"
    }
    // Otherwise, return "YES"
    return "YES"
}