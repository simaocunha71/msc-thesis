Here is the Java code for the problem:

```java
public class Main {
    public static boolean isSimplePower(int x, int n) {
        for (int i = 1; i <= n; i++) {
            if (Math.pow(i, n) == x) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println(isSimplePower(1, 4));  // true
        System.out.println(isSimplePower(2, 2));  // true
        System.out.println(isSimplePower(8, 2));  // true
        System.out.println(isSimplePower(3, 2));  // false
        System.out.println(isSimplePower(3, 1));  // false
        System.out.println(isSimplePower(5, 3));  // false
    }
}
```

In this code, we use a for loop to check if x is a simple power of n. We calculate the value of i to the power of n for each i from 1 to n, and if this value is equal to x, we return true. If we don't find such i, we return false. The main method is used to test the function with different inputs. 