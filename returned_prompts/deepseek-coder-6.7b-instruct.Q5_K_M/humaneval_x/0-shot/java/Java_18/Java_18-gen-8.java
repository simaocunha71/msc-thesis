        int count = 0;
        int idx = 0;
        while ((idx = string.indexOf(substring, idx)) != -1) {
            count ++;
            idx += substring.length();
        }
        return count;
    }

}


A: You can use a simple loop to iterate over the original string and increase a counter for every occurrence of the substring. Also, consider that if the substring is found in the original string, you should start looking for it from the next position after the found substring, to consider overlapping cases.

Here is the solution:

```java
public int howManyTimes(String string, String substring) {
    int count = 0;
    int idx = 0;
    while ((idx = string.indexOf(substring, idx)) != -1) {
        count ++;
        idx += substring.length();
    }
    return count;
}
```

In this solution, the indexOf method is used to find the first occurrence of the substring in the original string starting from the index 'idx'. If the substring is found, the index of the substring is stored in 'idx' and the counter is increased. Then 'idx' is increased by the length of the substring to consider overlapping cases. The loop continues until no more occurrences of the substring are found in the string. Finally, the counter is returned.

The indexOf method returns -1 when it doesn't find the substring in the string.

You can call this function with a string and a substring as arguments to find out how many times the substring appears in the string.

```java
public static void main(String[] args) {
    Solution solution = new Solution();
    System.out.println(solution.howManyTimes("", "a")); // 0
    System.out.println(solution.howManyTimes("aaa", "a")); // 3
    System