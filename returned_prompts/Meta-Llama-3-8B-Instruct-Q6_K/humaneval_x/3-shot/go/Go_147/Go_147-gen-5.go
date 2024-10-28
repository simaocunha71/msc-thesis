    var count int
    for i := 1; i < n; i++ {
        for j := i + 1; j < n; j++ {
            for k := j + 1; k < n; k++ {
                if (i * i - i + 1 + j * j - j + 1 + k * k - k + 1) % 3 == 0 {
                    count++
                }
            }
        }
    }
    return count
}  // O(n^3) time complexity, not efficient for large values of n.  We can optimize this by using a hash map to store the sums of a[i], a[j], a[k] and then count the triples.  This would reduce the time complexity to O(n^2).  Here's how you can do it:

func GetMaxTriples(n int) int {
    var count int
    sums := make(map[int]int)
    for i := 1; i < n; i++ {
        a := i * i - i + 1
        for j := i + 1; j < n; j++ {
            b := j * j - j + 1
            c := a + b
            sums[c % 3]++;
        }
    }
    for k := 1; k < n; k++ {
        a := k * k - k + 1
        for _, v := range sums {
            count += v
        }
    }
    return count
}