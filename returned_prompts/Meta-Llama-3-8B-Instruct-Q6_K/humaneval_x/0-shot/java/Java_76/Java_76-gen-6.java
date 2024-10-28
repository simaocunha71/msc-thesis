You can use the following code to solve the problem:

```java
public boolean isSimplePower(int x, int n) {
    for (int i = 1; i <= Math.sqrt(x); i++) {
        if ((int) Math.pow(n, i) == x) {
            return true;
        }
    }
    return false;
}
```

This function iterates over all possible powers of n, from 1 to the square root of x. If it finds a power that is equal to x, it returns true. If it doesn't find any such power, it returns false. The `Math.pow` function is used to calculate the power, and the cast to `(int)` is used to truncate the result to an integer, because the `Math.pow` function returns a double. The `Math.sqrt` function is used to calculate the square root of x, which is used to limit the range of the loop. This is because a larger power of n cannot be equal to x, because it would be greater than x. 

This function has a time complexity of O(sqrt(x)), which is efficient enough for most practical purposes. However, if you need a more efficient solution, you could use a logarithmic algorithm to find the power, or use a more advanced mathematical technique to solve the problem. 

For example, you could use the following code to solve the problem:

```java
public boolean isSimplePower(int x, int n) {
    int logN = (int) Math.log(x) / Math.log(n);
    return (int) Math.pow(n, logN) == x;
}
```

This function uses the logarithm function to calculate the power of n that is closest to x. If this power is exactly equal to x, it returns true. If it's not equal to x, it returns false. This function has a time complexity of O(1), which is much more efficient than the previous function. However, it's not as simple to understand, and it may not work correctly for all inputs. 

In general, the choice of algorithm depends on the specific requirements of your problem, such as the range of inputs, the desired level of precision, and the available resources. 

For example, if you need to solve the problem for very large inputs, you may need to use a logarithmic algorithm to avoid overflow. If you need to solve the problem for very small inputs, you may need to use a simple iterative algorithm to avoid underflow. 

In any case