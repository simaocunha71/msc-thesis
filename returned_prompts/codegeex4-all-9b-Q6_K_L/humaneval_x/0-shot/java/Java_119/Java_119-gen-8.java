```java
public String matchParens(List<String> lst) {
    int open = 0;
    for (String s : lst) {
        for (char c : s.toCharArray()) {
            if (c == '(') {
                open++;
            } else {
                if (open == 0) {
                    return "No";
                }
                open--;
            }
        }
    }
    return open == 0 ? "Yes" : "No";
}
```