Here is a solution using Java:

```java
public boolean isSimplePower(int x, int n) {
    if(x == 1 || n == 1) {
        return true;
    }
    int power = x;
    while(power < Integer.MAX_VALUE) {
        power *= n;
        if(power == x) {
            return true;
        }
    }
    return false;
}
```

Explanation:
- We first handle the special cases where x or n is 1. In both cases, x is a simple power of n.
- Then, we initialize a variable power to x.
- We enter a loop where we multiply power by n until it is equal to x or until it reaches the maximum value of an integer.
- If power is equal to x, we return true because x is a simple power of n.
- If the loop ends without finding a power that is equal to x, we return false because x is not a simple power of n.