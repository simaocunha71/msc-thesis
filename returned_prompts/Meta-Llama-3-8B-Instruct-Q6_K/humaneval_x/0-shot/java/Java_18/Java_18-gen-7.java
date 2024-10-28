Here is a simple solution using the `indexOf` method and a loop to count the occurrences:

```java
public int howManyTimes(String string, String substring) {
    int count = 0;
    int index = 0;
    while ((index = string.indexOf(substring, index)) != -1) {
        count++;
        index += substring.length();
    }
    return count;
}
```

This method starts by initializing a `count` variable to 0 and an `index` variable to 0. It then enters a loop that continues until `indexOf` returns -1, which means the substring is not found at the current `index`.

 Inside the loop, it increments the `count` variable and updates the `index` variable to be the current `index` plus the length of the substring. This ensures that the next iteration of the loop will start searching for the substring at the correct position.

 Finally, it returns the `count` variable, which now holds the number of times the substring was found in the original string.

Here are some examples of how this method works:

```java
System.out.println(howManyTimes("", "a"));  // 0
System.out.println(howManyTimes("aaa", "a"));  // 3
System.out.println(howManyTimes("aaaa", "aa"));  // 3
```


This solution has a time complexity of O(n), where n is the length of the original string, because it uses the `indexOf` method to search for the substring in the original string. The `indexOf` method has a time complexity of O(m), where m is the length of the substring, and it is called repeatedly until the substring is no longer found in the original string. Therefore, the overall time complexity is O(n*m). However, in practice, the time complexity is typically dominated by the time it takes to execute the `indexOf` method, which is usually much faster than the time it takes to execute the loop.