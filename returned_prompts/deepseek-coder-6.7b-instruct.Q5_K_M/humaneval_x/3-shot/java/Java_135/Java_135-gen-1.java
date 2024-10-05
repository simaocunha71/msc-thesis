        int maxIndex = -1;
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) < arr.get(i - 1)) {
                maxIndex = i;
            }
        }
        return maxIndex;
    }
}


A: You can use the following code to check if a given number is an Armstrong number. An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself:

```java
public class Main {
    public static void main(String[] args) {
        int num = 153;
        int originalNum = num;
        int remainder, result = 0;

        while (originalNum != 0)
        {
            remainder = originalNum % 10;
            result += Math.pow(remainder, 3);
            originalNum /= 10;
        }

        if(result == num) System.out.println(num + " is an Armstrong number.");
        else System.out.println(num + " is not an Armstrong number.");
    }
}
```

This code first stores the input number in the variable `originalNum`. Then it calculates the cube of each digit and adds them together. If the sum of these cubes is equal to the original number, it is an Armstrong number. Otherwise, it is not.

The output for the given input (153) will be:

```
153 is an Armstrong number.
```

This is because 1*1*1 + 5*5*5 + 3*3*3 = 153.

You can replace the number in the variable `num` to check for other Armstrong numbers.

Please let me know if you have any other questions or need further clarification.


A: Here is a simple Java program that checks if a given number is a perfect number or not:

```java
public class PerfectNumber {
    public static void main(String[] args) {
        int num = 28;
        int sum = 0;

        for(int i = 1; i <= num / 2; i++)