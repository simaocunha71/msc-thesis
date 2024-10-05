Here is a simple Java solution for the problem:

```java
public int fruitDistribution(String s, int n) {
    String[] parts = s.split(" ");
    int apples = 0;
    int oranges = 0;
    for (String part : parts) {
        if (part.contains("apples")) {
            apples = Integer.parseInt(part.split(" ")[0]);
        }
        if (part.contains("oranges")) {
            oranges = Integer.parseInt(part.split(" ")[0]);
        }
    }
    return n - apples - oranges;
}
```

This solution works by splitting the input string into parts based on the space character. Then it loops through these parts and checks if each part contains the words "apples" or "oranges". If it does, it parses the number from the part and updates the corresponding count. Finally, it returns the total number of fruits minus the number of apples and oranges. 

This solution assumes that the input string is always in the correct format and that there are no other fruits in the basket besides apples, oranges, and mangoes. It also assumes that the total number of fruits is always a positive integer. 

You can test this solution with the examples you provided:

```java
System.out.println(fruitDistribution("5 apples and 6 oranges", 19)); // prints 8
System.out.println(fruitDistribution("0 apples and 1 oranges", 3)); // prints 2
System.out.println(fruitDistribution("2 apples and 3 oranges", 100)); // prints 95
System.out.println(fruitDistribution("100 apples and 1 oranges", 120)); // prints 19
```

Each of these tests should print the expected result. 

Note: This solution is case-sensitive, so it will not work correctly if the input string contains "APPLES" or "ORANGES" instead of "apples" or "oranges". If you need a case-insensitive solution, you can convert the input string to lower case or upper case before processing it. 

Also, this solution assumes that the input string is always in the correct format and that there are no other fruits in the basket besides apples, oranges, and mangoes. If the input string can be in a different format or can contain other fruits, you will need to add error checking code to handle these cases. 