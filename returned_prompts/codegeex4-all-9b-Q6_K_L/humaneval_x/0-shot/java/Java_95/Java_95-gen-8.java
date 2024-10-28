```java
public boolean checkDictCase(Map<Object, Object> dict) {
    if (dict.isEmpty()) {
        return false;
    }

    boolean isLower = true;
    boolean isUpper = true;

    for (Object key : dict.keySet()) {
        if (!(key instanceof String)) {
            return false;
        }

        String keyStr = (String) key;

        if (!keyStr.equals(keyStr.toLowerCase())) {
            isLower = false;
        }

        if (!keyStr.equals(keyStr.toUpperCase())) {
            isUpper = false;
        }
    }

    return isLower || isUpper;
}
```