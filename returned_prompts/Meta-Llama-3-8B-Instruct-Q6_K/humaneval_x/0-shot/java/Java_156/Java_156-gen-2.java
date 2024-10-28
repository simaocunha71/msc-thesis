Here is the solution:
```java
public String intToMiniRoman(int number) {
    Map<Integer, String> romanMap = new HashMap<>();
    romanMap.put(1000, "m");
    romanMap.put(900, "cm");
    romanMap.put(500, "d");
    romanMap.put(400, "cd");
    romanMap.put(100, "c");
    romanMap.put(90, "xc");
    romanMap.put(50, "l");
    romanMap.put(40, "xl");
    romanMap.put(10, "x");
    romanMap.put(9, "ix");
    romanMap.put(5, "v");
    romanMap.put(4, "iv");
    romanMap.put(1, "i");

    StringBuilder result = new StringBuilder();
    for (Map.Entry<Integer, String> entry : romanMap.entrySet()) {
        while (number >= entry.getKey()) {
            number -= entry.getKey();
            result.append(entry.getValue());
        }
    }
    return result.toString().toLowerCase();
}
```
Explanation:

*   We create a `HashMap` called `romanMap` to store the Roman numeral values and their corresponding integer values.
*   We iterate over the `romanMap` and for each entry, we subtract the integer value from the input number as many times as possible (using the `while` loop) and append the corresponding Roman numeral to the `result` `StringBuilder`.
*   Finally, we return the `result` as a lowercase string using the `toString()` method.

This solution works for numbers within the range of 1 to 1000, as per the problem restrictions. For numbers outside this range, you would need to extend the `romanMap` to include additional entries.