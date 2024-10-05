```java
public String removeVowels(String text) {
    String vowels = "aeiouAEIOU";
    StringBuilder result = new StringBuilder();
    for (char c : text.toCharArray()) {
        if (!vowels.indexOf(c) != -1) {
            result.append(c);
        }
    }
    return result.toString();
}
```