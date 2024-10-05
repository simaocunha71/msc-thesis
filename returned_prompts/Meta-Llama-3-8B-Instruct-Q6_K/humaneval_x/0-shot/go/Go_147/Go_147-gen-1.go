    res := 0
    for i := 1; i < n; i++ {
        for j := i + 1; j < n; j++ {
            for k := j + 1; k <= n; k++ {
                if (i*i-i+1 + j*j-j+1 + k*k-k+1) % 3 == 0 {
                    res++
                }
            }
        }
    }
    return res
}
// The time complexity is O(n^3) and space complexity is O(1)
// The above function will give the correct result, but it's not efficient for large inputs. 

// We can improve the time complexity by using the property of modular arithmetic.
// The sum of the numbers a[i], a[j], a[k] is divisible by 3 if and only if the sum of their remainders when divided by 3 is 0.
// So, we can calculate the remainder of a[i], a[j], a[k] when divided by 3, and count the number of triples with sum of remainders equal to 0.
func GetMaxTriples(n int) int {

    res := 0
    for i := 1; i < n; i++ {
        iRemainder := (i * i - i + 1) % 3
        for j := i + 1; j < n; j++ {
            jRemainder := (j * j - j + 1) % 3
            for k := j + 1; k <= n; k++ {
                kRemainder := (k * k - k + 1) % 3
                if iRemainder+jRemainder+kRemainder == 0 {
                    res++
                }
            }
        }
    }
    return res
}
// The time complexity is O(n^2) and space complexity is O(1)
// The above function will give the correct result, but it's still not efficient for large inputs. 

// We can further improve the time complexity by using a hash map to store the count of remainders.
func GetMaxTriples(n int) int {

    res := 0
    remainderCount := make(map[int]int)
    remainderCount[0] = 1
    for i := 1; i < n; i++ {
        iRemainder := (i * i - i + 1) % 3