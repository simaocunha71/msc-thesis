    for i := 2; i <= n; i += 2 {
        sum := 0
        for j := 2; j <= n; j += 2 {
            sum += j
            if sum == n {
                return true
            }
            if sum > n {
                break
            }
        }
    }
    return false
} // O(n^2) time complexity, not efficient for large inputs. Better solution should be O(n) time complexity. 



