```java
public class Solution {
    public String StrongestExtension(String class_name, List<String> extensions) {
        if(extensions == null || extensions.isEmpty()) {
            return class_name;
        }
        String strongest_extension = extensions.get(0);
        int strongest_extension_strength = countStrength(strongest_extension);
        for(String extension : extensions) {
            int extension_strength = countStrength(extension);
            if(extension_strength > strongest_extension_strength) {
                strongest_extension = extension;
                strongest_extension_strength = extension_strength;
            } else if(extension_strength == strongest_extension_strength) {
                if(extension.compareTo(strongest_extension) < 0) {
                    strongest_extension = extension;
                }
            }
        }
        return class_name + "." + strongest_extension;
    }

    private int countStrength(String str) {
        int uppercase = 0, lowercase = 0;
        for(char c : str.toCharArray()) {
            if(Character.isUpperCase(c)) {
                uppercase++;
            } else if(Character.isLowerCase(c)) {
                lowercase++;
            }
        }
        return uppercase - lowercase;
    }
}
```