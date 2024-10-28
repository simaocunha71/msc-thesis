Here is a Java solution for the problem:

```java
public class Solution {
    public String StrongestExtension(String class_name, List<String> extensions) {
        String strongestExtension = "";
        int strongestStrength = Integer.MIN_VALUE;
        
        for (String extension : extensions) {
            int cap = 0;
            int sm = 0;
            for (char c : extension.toCharArray()) {
                if (Character.isUpperCase(c)) {
                    cap++;
                } else if (Character.isLowerCase(c)) {
                    sm++;
                }
            }
            int strength = cap - sm;
            if (strength > strongestStrength) {
                strongestStrength = strength;
                strongestExtension = extension;
            } else if (strength == strongestStrength) {
                strongestExtension = extension;
            }
        }
        return class_name + "." + strongestExtension;
    }
}
```

This solution iterates over each extension, calculates its strength by counting the number of uppercase and lowercase letters, and then compares its strength with the strongest strength found so far. If the strength is higher, it updates the strongestExtension. If the strength is the same, it also updates the strongestExtension. Finally, it returns the class name followed by the strongest extension. 