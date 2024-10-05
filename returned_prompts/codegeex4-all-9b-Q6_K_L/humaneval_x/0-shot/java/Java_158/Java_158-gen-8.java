```java
public String findMax(List<String> words) {
    String max = "";
    for (String word : words) {
        if (word.length() > max.length() || (word.length() == max.length() && word.compareTo(max) < 0)) {
            max = word;
        }
    }
    return max;
}
```