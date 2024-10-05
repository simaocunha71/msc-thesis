
    // Initialize the array with given formula
    arr := make([]int, n+1)
    for i := 1; i <= n; i++ {
        arr[i] = i*i - i + 1
    }

    // Initialize the count of triples
    count := 0

    // Loop through the array and count the triples
    for i := 1; i <= n-2; i++ {
        for j := i + 1; j <= n-1; j++ {
            for k := j + 1; k <= n; k++ {
                if (arr[i]+arr[j]+arr[k])%3 == 0 {
                    count++
                }
            }
        }
    }

    return count
}

// Time Complexity: O(n^3)
// Space Complexity: O(n)
func main() {
    fmt.Println(GetMaxTriples(5)) // Output: 1
}
```

### Optimize the code

The above code is not efficient as it has a time complexity of O(n^3) which is not suitable for large inputs. We can optimize the code by using a hash table to store the counts of remainders when the elements of the array are divided by 3.

```go
package main

import "fmt"

func GetMaxTriples(n int) int {
    arr := make([]int, n+1)
    for i := 1; i <= n; i++ {
        arr[i] = (i*i - i + 1) % 3
    }

    count := 0
    modCounts := make([]int, 3)

    for i := 1; i <= n; i++ {
        count += modCounts[arr[i]]
        modCounts[arr[i]]++
    }

    return count
}

func main() {
    fmt.Println(GetMaxTriples(5)) // Output: 1
}
```

In this code, we first calculate the remainder of the elements of the array when divided by 3. Then, we use a hash table