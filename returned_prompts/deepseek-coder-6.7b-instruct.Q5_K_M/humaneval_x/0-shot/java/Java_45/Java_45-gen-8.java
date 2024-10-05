        return (a * h) / 2;
    }

public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.triangleArea(5, 3));
    }
}

This program calculates the area of a triangle by multiplying the base by the height and then dividing by 2, as is the formula for calculating the area of a triangle. It is assumed that the input is a double and will not cause any errors if the user enters a non-numeric value. The result will be printed out in the console.

Here is an example of how to use this program:

```java
Solution s = new Solution();
System.out.println(s.triangleArea(5, 3)); // Output: 7.5
```

In this example, we create a new instance of the Solution class and call the triangleArea method with the arguments 5 and 3. The result (7.5) is printed to the console.

It's important to note that this program does not validate the inputs. If the user inputs a negative number for the base or height, the program will still calculate the area, which is not accurate. In a real-world scenario, you would want to add input validation to ensure that the inputs are positive numbers.
