        if(!(x instanceof Integer) || !(y instanceof Integer) || !(z instanceof Integer)){
            return false;
        }

        int a = (Integer)x;
        int b = (Integer)y;
        int c = (Integer)z;

        return a == b+c || b == a+c || c == a+b;
    }
}

This solution checks if all three inputs are integers and then checks if any of them is equal to the sum of the other two.

The solution is based on the problem statement and does not take into account edge cases or possible floating point numbers.

The solution uses casting to convert the Objects to Integers, and then checks if any of them equals the sum of the other two. This solution assumes that the inputs are always three integers.

Also, please note that the method signature is changed to accept Objects instead of ints to allow for input of any type.
*/

// Testing
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.anyInt(5, 2, 7)); // -> true
        System.out.println(sol.anyInt(3, 2, 2)); // -> false
        System.out.println(sol.anyInt(3, -2, 1)); // -> true
        System.out.println(sol.anyInt(3.6, -2.2, 2)); // -> false
    }
}

/*
Output:
true
false
true
false
*/
```

## Code Explanation

This code is a simple solution to the problem. The function `anyInt()` takes in three parameters of type `Object`. It then checks if all three parameters are instances of the `Integer` class. If not, it returns `false`.

If all parameters are integers, it casts them to `int` types and checks if any of them is equal to the sum of the other two. If it finds such a number, it returns `true`; otherwise, it returns `false`.

## Testing

The testing part of the code creates an instance of the `Solution` class and calls the