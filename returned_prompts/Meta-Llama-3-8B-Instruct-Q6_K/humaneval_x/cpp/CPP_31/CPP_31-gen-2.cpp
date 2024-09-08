    if(n <= 1)
        return false;
    if(n <= 3)
        return true;
    if(n % 2 == 0 || n % 3 == 0)
        return false;
    for(long long i = 5; i * i <= n; i += 6){
        if(n % i == 0 || n % (i + 2) == 0)
            return false;
    }
    return true;
}
int main()
{
    printf("%d\n",is_prime(6));
    printf("%d\n",is_prime(101));
    printf("%d\n",is_prime(11));
    printf("%d\n",is_prime(13441));
    printf("%d\n",is_prime(61));
    printf("%d\n",is_prime(4));
    printf("%d\n",is_prime(1));
    return 0;
}
B:
Here is the Python code for the same:

```
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

print(is_prime(6))
print(is_prime(101))
print(is_prime(11))
print(is_prime(13441))
print(is_prime(61))
print(is_prime(4))
print(is_prime(1))
```

C:
Here is the Java code for the same:

```java
public class Main {
    public static boolean isPrime(long n) {
        if (n <= 1)
            return false;
        if (n <= 3)
            return true;
        if (n % 2 == 0 || n % 3 == 0)
            return false;
        for (long i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0)
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(isPrime(6));
        System.out.println(isPrime(101));
        System.out.println(isPrime(11));
        System.out.println(is