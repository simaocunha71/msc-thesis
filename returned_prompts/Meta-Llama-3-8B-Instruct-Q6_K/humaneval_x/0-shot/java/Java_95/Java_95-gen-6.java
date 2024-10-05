Here is the solution to the problem:
```java
public boolean checkDictCase(Map<Object, Object> dict) {
    if (dict.isEmpty()) {
        return false;
    }
    boolean allLower = true;
    boolean allUpper = true;
    for (Map.Entry<Object, Object> entry : dict.entrySet()) {
        String key = entry.getKey().toString();
        if (!allLower) {
            allLower = key.equals(key.toLowerCase());
        }
        if (!allUpper) {
            allUpper = key.equals(key.toUpperCase());
        }
        if (!allLower && !allUpper) {
            return false;
        }
    }
    return allLower || allUpper;
}
```
The function `checkDictCase` takes a map as an argument and returns a boolean value. It first checks if the map is empty. If it is, the function returns `false`. Then it initializes two boolean variables, `allLower` and `allUpper`, to `true`. These variables will be used to keep track of whether all keys in the map are in lower case or upper case.

The function then iterates over each entry in the map. For each entry, it converts the key to both lower case and upper case and checks if the original key is equal to the converted key. If the key is not equal to the lower case or upper case version, the function sets `allLower` or `allUpper` to `false`, depending on whether the key is equal to the lower case version or the upper case version.

If the function finds a key that does not match the lower case or upper case pattern, it immediately returns `false`. If it iterates over all entries without finding a key that does not match the pattern, it returns `true` if either `allLower` or `allUpper` is `true`, indicating that all keys in the map are in lower case or upper case. If neither `allLower` nor `allUpper` is `true`, the function returns `false`, indicating that the map contains keys in both lower case and upper case.