```go
func Exchange(lst1, lst2 []int) string {
    evenCount := 0
    for _, num := range lst1 {
        if num%2 == 0 {
            evenCount++
        }
    }
    for _, num := range lst2 {
        if num%2 == 0 {
            evenCount++
        }
    }
    if evenCount >= len(lst1) {
        return "YES"
    }
    return "NO"
}
```


Explanation:
This function iterates through both lists and counts the number of even numbers in each list. If the total count of even numbers is greater than or equal to the length of lst1, it returns "YES", indicating that it's possible to make lst1 a list of only even numbers by exchanging elements with lst2. Otherwise, it returns "NO". The time complexity is O(n), where n is the total number of elements in both lists. The space complexity is O(1), as we only use a constant amount of space to store the count of even numbers.