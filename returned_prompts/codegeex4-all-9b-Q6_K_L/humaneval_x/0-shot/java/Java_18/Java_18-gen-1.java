You can solve this problem by using the `indexOf` method from the Java String class. This method returns the index of the first occurrence of the specified substring in the string. If the substring is not found, it returns `-1`.

To count the number of times a substring appears in a string, you can use a loop. In each iteration of the loop, you call the `indexOf` method to find the next occurrence of the substring. If the `indexOf` method returns `-1`, it means that the substring has not been found, so you can stop the loop. Otherwise, you update the index to start searching for the next occurrence of the substring.

Here is the implementation of the `howManyTimes` method:

```java
public int howManyTimes(String string, String substring) {
    int count = 0;
    int index = 0;
    while (true) {
        index = string.indexOf(substring, index);
        if (index == -1) {
            break;
        }
        count++;
        index++;
    }
    return count;
}
```

In this implementation, the `count` variable keeps track of the number of times the substring appears in the string. The `index` variable is used as the starting point for the search in each iteration of the loop. After finding an occurrence of the substring, the `index` is incremented by `1` to start searching for the next occurrence.

The `indexOf` method has two parameters: the substring to search for and the starting index. By passing the current value of the `index` variable as the starting index, you ensure that the search starts from the position after the last found occurrence of the substring. This allows you to count overlapping occurrences of the substring.