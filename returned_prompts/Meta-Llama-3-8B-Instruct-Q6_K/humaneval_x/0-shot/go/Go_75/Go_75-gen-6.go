```
package main

import (
    "fmt"
)

func IsMultiplyPrime(a int) bool {
    for i := 2; i <= a; i++ {
        for j := i; j <= a; j++ {
            for k := j; k <= a; k++ {
                if i*j*k == a {
                    for primeCheck := 2; primeCheck*primeCheck <= i; primeCheck++ {
                        if i%primeCheck == 0 {
                            break
                        }
                    }
                    if i <= 1 {
                        break
                    }
                    for primeCheck := 2; primeCheck*primeCheck <= j; primeCheck++ {
                        if j%primeCheck == 0 {
                            break
                        }
                    }
                    if j <= 1 {
                        break
                    }
                    for primeCheck := 2; primeCheck*primeCheck <= k; primeCheck++ {
                        if k%primeCheck == 0 {
                            break
                        }
                    }
                    if k <= 1 {
                        break
                    }
                    return true
                }
            }
        }
    }
    return false
}

func main() {
    fmt.Println(IsMultiplyPrime(30)) // prints: true
    fmt.Println(IsMultiplyPrime(45)) // prints: true
    fmt.Println(IsMultiplyPrime(48)) // prints: false
}
```

B:
```
package main

import (
    "fmt"
)

func IsMultiplyPrime(a int) bool {
    for i := 2; i <= a; i++ {
        for j := 2; j <= a/i; j++ {
            k := a / (i * j)
            if i*j*k == a {
                for primeCheck := 2; primeCheck*primeCheck <= i; primeCheck++ {
                    if i%primeCheck == 0 {
                        break
                    }
                }
                if i <= 1 {
                    break
                }
                for primeCheck := 2; primeCheck*primeCheck <= j; primeCheck++ {
                    if j%primeCheck == 0 {
                        break
                    }
                }
                if j <= 1 {
                    break
                }
                for primeCheck := 2; primeCheck*primeCheck <= k; primeCheck++ {
                    if k%primeCheck == 0 {
                        break
                    }
                }
                if k <= 1 {
                    break
                }
                return true
            }
        }
    }
    return false