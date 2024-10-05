    int count1 = 0, count2 = 0;

    for (String s : lst1) {
        count1 += s.length();
    }

    for (String s : lst2) {
        count2 += s.length();
    }

    if (count1 < count2) {
        return lst1;
    } else if (count1 > count2) {
        return lst2;
    } else {
        return lst1;
    }
    }
}


A: You're almost there. Instead of just returning the list with the smaller length, you should return the list with the smaller total number of characters.
Here's the corrected solution:
public List<String> totalMatch(List<String> lst1, List<String> lst2) {
    int sum1 = 0, sum2 = 0;

    for (String s : lst1) {
        sum1 += s.length();
    }

    for (String s : lst2) {
        sum2 += s.length();
    }

    if (sum1 < sum2) {
        return lst1;
    } else if (sum1 > sum2) {
        return lst2;
    } else {
        return lst1;
    }
}

In this solution, we first compute the total number of characters in lst1 and lst2 respectively. We then compare these sums to determine which list has the smaller total number of characters. If lst1 has a smaller total number of characters, we return lst1. If lst2 has a smaller total number of characters, we return lst2. If the sums are equal, we return lst1.

A: In Java 8, you can use the mapToInt and sum methods to simplify the code:

```java
import java.util.*;
import java.util.stream.*;

class Solution {
    public List<String> totalMatch(List<String> lst1, List<String> lst2) {
        int sum1 = lst1.stream().mapToInt(String::length).sum();
        int sum2 = lst2.stream().mapToInt(String