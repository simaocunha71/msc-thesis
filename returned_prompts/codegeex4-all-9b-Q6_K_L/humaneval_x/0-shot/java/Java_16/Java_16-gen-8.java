Here is a Java solution using a HashSet. It converts the string to lowercase and then adds each character to the set. The size of the set represents the number of distinct characters in the string.

```java
public int countDistinctCharacters(String string) {
    HashSet<Character> distinctCharacters = new HashSet<Character>();
    string = string.toLowerCase();
    for(int i=0; i<string.length(); i++){
        distinctCharacters.add(string.charAt(i));
    }
    return distinctCharacters.size();
}
```

This will work for any string, including those with spaces, punctuation, etc. It will not count duplicate characters. If you want to count duplicates, you can use a HashMap instead of a HashSet.

```java
public int countDistinctCharacters(String string) {
    HashMap<Character, Integer> distinctCharacters = new HashMap<Character, Integer>();
    string = string.toLowerCase();
    for(int i=0; i<string.length(); i++){
        distinctCharacters.put(string.charAt(i), 1);
    }
    return distinctCharacters.size();
}
```