```java
public String removeVowels(String text) {
    Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
    StringBuilder sb = new StringBuilder();
    for (char c : text.toCharArray()) {
        if (!vowels.contains(c)) {
            sb.append(c);
        }
    }
    return sb.toString();
}
```