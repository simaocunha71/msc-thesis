

    largest = 2
    while n % 2 == 0:
        n = n / 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            largest = i
            n = n / i

    if n > 2:
        largest = n

    return int(largest)


if __name__ == "__main__":
    import doctest

    doctest.testmod()



```



## Java

```java
public class Main {

    public static void main(String[] args) {
        System.out.println(largestPrimeFactor(13195));  // Output: 29
        System.out.println(largestPrimeFactor(2048));   // Output: 2
    }

    public static int largestPrimeFactor(int n) {
        int largest = -1;

        while (n % 2 == 0) {
            largest = 2;
            n >>= 1;
        }

        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            while (n % i == 0) {
                largest = i;
                n = n / i;
            }
        }

        if (n > 2) {
            largest = n;
        }

        return largest;
    }
}

```



## JavaScript

```javascript
function largestPrimeFactor(n) {
    let largest = 2;

    while (n % 2 === 0) {
        n = n / 2;
    }

    for (let i = 3; i <= Math.sqrt(n); i += 2) {
        while (n % i === 0) {
            largest = i;
            n = n / i;
        }
    }

    if (n > 2) {
        largest = n;
    }

    return largest;
}

console.log(largestPrimeFactor(13195));  // Output: 29
console