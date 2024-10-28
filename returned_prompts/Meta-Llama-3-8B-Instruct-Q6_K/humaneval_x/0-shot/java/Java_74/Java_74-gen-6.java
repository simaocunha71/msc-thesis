```java
public List<String> totalMatch(List<String> lst1, List<String> lst2) {
    int sum1 = 0;
    for (String s : lst1) {
        sum1 += s.length();
    }
    int sum2 = 0;
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
```
The function iterates over the strings in both lists, calculating the total number of characters in each list. It then compares these sums, returning the list with the smaller sum. If the sums are equal, it returns the first list. This ensures that if the lists have the same number of characters, the first list is returned. 

Note: This function has a time complexity of O(n) where n is the total number of strings in the two lists, as it iterates over each string in the lists once. The space complexity is O(1), as it only uses a constant amount of space to store the sums. 