        int a = 1, b = 1;
        int count = 0;
        while (true) {
            if (isPrime(b)) {
                count++;
                if (count == n) {
                    return b;
                }
            }
            a = a + b;
            b = a;
        }
    }

    public boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
}
}S:

```
python
def primeFib(n):
    a, b = 1, 1
    count = 0
    while True:
        if isPrime(b):
            count += 1
            if count == n:
                return b
        a, b = b, a + b
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```S:

```
java
class Solution {
    public int primeFib(int n) {
        int a = 1, b = 1;
        int count = 0;
        while (true) {
            if (isPrime(b)) {
                count++;
                if (count == n) {
                    return b;
                }
            }
            a = a + b;
            b = a;
        }
    }

    public boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```S:

```
python
def primeFib(n):
    a, b = 1, 1
    count = 0
    while True:
        if isPrime(b):
            count += 1
            if count == n:
                return b
        a, b = b, a + b

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5)