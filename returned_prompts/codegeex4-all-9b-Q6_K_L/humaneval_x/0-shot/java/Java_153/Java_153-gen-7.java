```java
import java.util.*;
import java.lang.*;

class Solution {
    public String StrongestExtension(String class_name, List<String> extensions) {
        int max = Integer.MIN_VALUE;
        String res = "";
        for (String extension : extensions) {
            int strength = getStrength(extension);
            if (strength > max) {
                max = strength;
                res = extension;
            }
        }
        return class_name + "." + res;
    }

    private int getStrength(String extension) {
        int cap = 0;
        int sm = 0;
        for (char c : extension.toCharArray()) {
            if (Character.isUpperCase(c)) cap++;
            else if (Character.isLowerCase(c)) sm++;
        }
        return cap - sm;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.StrongestExtension("my_class", Arrays.asList("AA", "Be", "CC"))); // "my_class.AA"
    }
}
```
