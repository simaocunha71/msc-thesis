Here is the Java code:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public String StrongestExtension(String class_name, List<String> extensions) {
        String strongest = "";
        int maxStrength = Integer.MIN_VALUE;
        for (String ext : extensions) {
            int strength = getStrength(ext);
            if (strength > maxStrength) {
                maxStrength = strength;
                strongest = ext;
            }
        }
        return class_name + "." + strongest;
    }

    private int getStrength(String extension) {
        int strength = 0;
        for (char c : extension.toCharArray()) {
            if (Character.isUpperCase(c)) {
                strength++;
            } else if (Character.isLowerCase(c)) {
                strength--;
            }
        }
        return strength;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.StrongestExtension("Slices", Arrays.asList("SErviNGSliCes", "Cheese", "StuFfed"))); // Slices.SErviNGSliCes
        System.out.println(sol.StrongestExtension("my_class", Arrays.asList("AA", "Be", "CC"))); // my_class.AA
    }
}
```

In this code, we first initialize `strongest` with the first extension and `maxStrength` with the strength of the first extension. Then we iterate over the rest of the extensions, calculating their strength and updating `strongest` and `maxStrength` if we find a stronger extension. Finally, we return the string in the format `ClassName.StrongestExtensionName`.