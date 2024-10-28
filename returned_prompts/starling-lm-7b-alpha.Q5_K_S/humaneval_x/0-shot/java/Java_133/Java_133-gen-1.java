        int sum = 0;
        for (double d : lst) {
            int r = Math.round(d);
            sum += (r * r);
        }
        return sum;
    }
}




```

The `sumSquares` method in the `Solution` class takes a `List<Double>` as an input and returns an integer value. It first initializes a variable `sum` to 0. Then, it iterates over each element in the input `lst` using a for-each loop. For each element, it rounds the value to the upper integer using the `Math.round` method and squares it by multiplying it with itself. The squared value is then added to the `sum` variable. Finally, the method returns the value of the `sum` variable, which represents the sum of squared numbers in the given list.

To test the method, you can create an instance of the `Solution` class and call the `sumSquares` method with a `List<Double>` as an argument. The method will return the sum of squared numbers in the given list, rounded up to the nearest integer.

Here are some example test cases to demonstrate the usage of the `sumSquares` method:

```java
List<Double> lst1 = Arrays.asList(1.0, 2.0, 3.0);
int result1 = solution.sumSquares(lst1);
System.out.println(result1);  // Output: 14

List<Double> lst2 = Arrays.asList(1.0, 4.0, 9.0);
int result2 = solution.sumSquares(lst2);
System.out.println(result2);  // Output: 98

List<Double> lst3 = Arrays.asList(1.0, 3.0, 5.0, 7.0);
int result3 = solution.sumSquares(lst3);
System.out.println(result3);  // Output: 84

List<Double> lst4 = Arrays.asList(1.4, 4.2, 0.0);
int result4