        int unitA = Math.abs(a % 10);
        int unitB = Math.abs(b % 10);
        return unitA * unitB;
    }
}

public class Main {
    public static void main(unitA, unitB) {
        Solution s = new Solution();
        System.out.println(s.multiply(148, 412));
        System.out.println(s.multiply(19, 28));
        System.out.println(s.multiply(2020, 1851));
        System.out.println(s.multiply(14, -15));
    }
}


A: It seems the problem lies in the Main class where you have called the multiply method with arguments which are not integers. 
Here is the corrected version of your code:

```java
public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.multiply(148, 412)); // should return 16
        System.out.println(s.multiply(19, 28)); // should return 72
        System.out.println(s.multiply(2020, 1851)); // should return 0
        System.out.println(s.multiply(14, -15)); // should return 20
    }
}
```

In the Main class, the main method should be declared with a String array as its parameter. It is the standard way to declare the main method in Java. The arguments that you pass to the multiply method should be integers.

And yes, the Solution class is correct. It takes two integers as input, finds the unit digits of those integers (by using the modulus operator), and returns the product of those unit digits. The Math.abs method is used to ensure that the unit digits are positive, even if the original numbers were negative.

The multiply method in the Solution class works perfectly.

Please check these corrections and let me know if you have any other questions.

