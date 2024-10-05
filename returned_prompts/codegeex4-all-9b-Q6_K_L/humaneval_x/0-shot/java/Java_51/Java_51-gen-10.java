```java
public String removeVowels(String text) {
    String result = "";
    for (char c : text.toCharArray()) {
        if (!"aeiouAEIOU".contains(String.valueOf(c))) {
            result += c;
        }
    }
    return result;
}
```