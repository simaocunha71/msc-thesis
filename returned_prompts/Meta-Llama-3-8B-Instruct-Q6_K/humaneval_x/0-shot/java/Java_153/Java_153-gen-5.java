Here is a Java solution:

```java
public class Solution {
    public String StrongestExtension(String class_name, List<String> extensions) {
        int max_strength = Integer.MIN_VALUE;
        String strongest_extension = "";
        
        for(String extension : extensions) {
            int cap = 0, sm = 0;
            for(char c : extension.toCharArray()) {
                if(Character.isUpperCase(c)) {
                    cap++;
                } else {
                    sm++;
                }
            }
            int strength = cap - sm;
            if(strength > max_strength) {
                max_strength = strength;
                strongest_extension = extension;
            }
        }
        
        return class_name + "." + strongest_extension;
    }
}
```

This solution iterates over each extension, calculates its strength by counting the number of uppercase and lowercase letters, and keeps track of the strongest extension. If there are multiple extensions with the same strength, it chooses the one that comes first in the list. Finally, it returns the class name and the strongest extension in the required format.