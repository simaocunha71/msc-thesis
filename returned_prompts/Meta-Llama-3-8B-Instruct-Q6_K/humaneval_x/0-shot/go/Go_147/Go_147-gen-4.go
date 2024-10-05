
The problem is asking to find the number of triples (a[i], a[j], a[k]) of an array a where i < j < k, and a[i] + a[j] + a[k] is a multiple of 3.

The approach is to create an array a of length n and calculate the value of a[i] for each i (1 ≤ i ≤ n). Then, for each i and j (1 ≤ i < j ≤ n), calculate the sum of a[i] and a[j]. If the sum is already in the hashmap, increment the answer by the hashmap value. Finally, return the answer.

Here is the implementation in Go:
```go
func GetMaxTriples(n int) int {
    var ans int
    var a []int
    for i := 1; i <= n; i++ {
        a = append(a, i*i - i + 1)
    }
    m := make(map[int]int)
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            sum := a[i] + a[j]
            if _, ok := m[sum]; ok {
                ans += m[sum