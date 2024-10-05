        int sum = 0;
        for(int i=1; i<=n; i++){
            sum += i;
        }
        return sum;
    }
}

class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();
        System.out.println(s.sumToN(30));
        System.out.println(s.sumToN(100));
        System.out.println(s.sumToN(5));
        System.out.println(s.sumToN(10));
        System.out.println(s.sumToN(1));
    }
}


A: Here is a simple Java program to sum numbers from 1 to n:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(sumToN(30)); // prints 465
        System.out.println(sumToN(100)); // prints 5050
        System.out.println(sumToN(5)); // prints 15
        System.out.println(sumToN(10)); // prints 55
        System.out.println(sumToN(1)); // prints 1
    }

    public static int sumToN(int n) {
        int sum = 0;
        for(int i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }
}
```

In the `sumToN` function, you are simply iterating from 1 to n (inclusive) and adding each number to the sum. The sum is then returned.

The `main` function is used to test the `sumToN` function. It calls `sumToN` with different values and prints the result.

I hope this helps you understand how to solve the problem.

Note: Please ensure that you have the correct Java Development Kit (JDK) installed and properly configured in your system to run and compile Java programs.

Note: The code provided above will work correctly for small inputs. However, for larger inputs (e.g.,