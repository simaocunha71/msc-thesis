Here is the Java solution for the problem:

```java
public String StrongestExtension(String class_name, List<String> extensions) {
    int max_strength = Integer.MIN_VALUE;
    String strongest_extension = "";
    for (String extension : extensions) {
        int uppercase_count = 0;
        int lowercase_count = 0;
        for (char c : extension.toCharArray()) {
            if (Character.isUpperCase(c)) {
                uppercase_count++;
            } else {
                lowercase_count++;
            }
        }
        int strength = uppercase_count - lowercase_count;
        if (strength > max_strength) {
            max_strength = strength;
            strongest_extension = extension;
        }
    }
    return class_name + "." + strongest_extension;
}
```

This function iterates through each extension in the list and calculates its strength by counting the number of uppercase and lowercase letters in the extension. It keeps track of the extension with the maximum strength and returns the class name followed by the strongest extension. If there are multiple extensions with the same maximum strength, it returns the one that comes first in the list. 