Here is the Java solution for the problem:

```java
public int fruitDistribution(String s, int n) {
    String[] parts = s.split(" ");
    int apples = 0;
    int oranges = 0;

    for (String part : parts) {
        if (part.endsWith("apples")) {
            apples = Integer.parseInt(part.replace("apples", ""));
        } else if (part.endsWith("oranges")) {
            oranges = Integer.parseInt(part.replace("oranges", ""));
        }
    }

    return n - apples - oranges;
}
```

This solution works by first splitting the input string into parts based on spaces. Then it iterates over these parts, checking if each part ends with "apples" or "oranges". If it does, it parses the part to get the number of apples or oranges. Finally, it returns the total number of fruits minus the number of apples and oranges. This will give the number of mango fruits.