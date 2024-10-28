
// Create a loop that starts at 2 and continues until n is greater than 1
// 1. In each iteration, check if the current number (i) divides n
// 2. If it does, n becomes n divided by i
// 3. Continue to the next iteration
// 4. When n is no longer divisible by i, increment i by 1 and continue
// 5. The value of i when n is no longer divisible by i is the largest prime factor of the original n

B:

return i
}

func main() {
    fmt.Println(LargestPrimeFactor(13195)) // 29
    fmt.Println(LargestPrimeFactor(2048))  // 2
}
```

## Python

```python
def LargestPrimeFactor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

print(LargestPrimeFactor(13195)) # 29
print(LargestPrimeFactor(2048))  # 2
```

## JavaScript

```javascript
function LargestPrimeFactor(n){
    let i = 2;
    while(i * i <= n){
        if(n % i){
            i++;
        } else {
            n = Math.floor(n / i);
        }
    }
    return n;
}

console.log(LargestPrimeFactor(13195)); // 29
console.log(LargestPrimeFactor(2048)); // 2
```

## Java

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(largestPrimeFactor(13195)); // 29
        System.out.println(largestPrimeFactor(2048)); // 2
    }

    public static int largestPrimeFactor(int n){
        int i = 2;