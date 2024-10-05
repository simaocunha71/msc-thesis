```java
import java.util.*;
import java.lang.*;

class Solution {
    public String StrongestExtension(String class_name, List<String> extensions) {
        String strongest = null;
        int maxStrength = Integer.MIN_VALUE;
        for (String extension : extensions) {
            int strength = calculateStrength(extension);
            if (strength > maxStrength) {
                maxStrength = strength;
                strongest = extension;
            }
        }
        return class_name + "." + strongest;
    }

    private int calculateStrength(String extension) {
        int uppercaseCount = 0;
        int lowercaseCount = 0;
        for (char c : extension.toCharArray()) {
            if (Character.isUpperCase(c)) {
                uppercaseCount++;
            } else if (Character.isLowerCase(c)) {
                lowercaseCount++;
            }
        }
        return uppercaseCount - lowercaseCount;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.StrongestExtension("my_class", Arrays.asList("AA", "Be", "CC"))); // Output: "my_class.AA"
    }
}
```
Explanation:
1. We iterate through each extension and calculate its strength using the `calculateStrength` method.
2. If the calculated strength is greater than the current maximum strength, we update the maximum strength and the strongest extension.
3. Finally, we return a string in the format "ClassName.StrongestExtensionName".
4. The `calculateStrength` method counts the number of uppercase and lowercase letters in the extension and returns their difference.