Here is a Java solution. The idea is to check the first string if it's already good, if it is, then we concatenate the second string and check if it's good. If the first string is not good, we then check the second string if it's already good, if it is, then we concatenate the first string and check if it's good. If neither string is good, we return "No".

```java
public String matchParens(List<String> lst) {
    String s1 = lst.get(0);
    String s2 = lst.get(1);
    if (isGood(s1)) {
        return isGood(s1 + s2) ? "Yes" : "No";
    } else if (isGood(s2)) {
        return isGood(s1 + s2) ? "Yes" : "No";
    } else {
        return "No";
    }
}

private boolean isGood(String s) {
    int count = 0;
    for (char c : s.toCharArray()) {
        if (c == '(') {
            count++;
        } else if (c == ')') {
            count--;
        }
        if (count < 0) {
            return false;
        }
    }
    return count == 0;
}
```

The `isGood` function checks if a string is good by counting the number of open and close parentheses. If at any point the number of close parentheses exceeds the number of open parentheses, the string is not good. At the end, the function checks if the number of open and close parentheses are equal. If not, the string is not good.