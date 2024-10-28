```java
public int fruitDistribution(String s, int n) {
    String[] fruit = s.split(" ");
    int apples = 0;
    int oranges = 0;
    for (String str : fruit) {
        if (str.endsWith("apples")) {
            apples = Integer.parseInt(str.replace("apples", ""));
        }
        if (str.endsWith("oranges")) {
            oranges = Integer.parseInt(str.replace("oranges", ""));
        }
    }
    return n - apples - oranges;
}
```


Explanation:
The function takes a string and an integer as parameters. The string represents the distribution of apples and oranges in a basket, and the integer represents the total number of fruits in the basket. The function splits the string into an array of strings using the " " character as the delimiter.

It then iterates over the array to find the number of apples and oranges. If a string ends with "apples", it parses the string to find the number of apples. If a string ends with "oranges", it parses the string to find the number of oranges.

Finally, the function returns the total number of fruits in the basket minus the number of apples and oranges, which is the number of mango fruits in the basket. The function handles cases where the string does not contain "apples" or "oranges" by not modifying the value of apples or oranges. If the string contains neither "apples" nor "oranges", the function still returns the total number of fruits in the basket.