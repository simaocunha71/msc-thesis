        String strongestExtensionName = extensions.get(0);
        int maxStrength = getStrength(extensions.get(0));
        for(String extension : extensions){
            int strength = getStrength(extension);
            if(strength > maxStrength){
                maxStrength = strength;
                strongestExtensionName = extension;
            }
        }
        return class_name + "." + strongestExtensionName;
    }

    private int getStrength(String extension){
        int capitalLetters = 0;
        int smallLetters = 0;
        for(char c : extension.toCharArray()){
            if(Character.isUpperCase(c)) capitalLetters++;
            else if(Character.isLowerCase(c)) smallLetters++;
        }
        return capitalLetters - smallLetters;
    }
}

This solution works by iterating through the list of extensions and calculating the strength of each one (difference between the count of uppercase letters and lowercase letters). The extension with the maximum strength is then returned as the strongest extension.


In this solution, getStrength method calculates the strength of the extension by counting the number of uppercase and lowercase letters in the extension. The strength is calculated by subtracting the count of lowercase letters from the count of uppercase letters.
*/

// Test this solution with the following code:

import java.util.*;

public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution solution = new Solution();
        System.out.println(solution.StrongestExtension("my_class", new ArrayList<>(Arrays.asList("AA", "Be", "CC"))));
    }
}

// Expected Output: "my_class.AA"

This test case checks for the strongest extension in a list of extensions where all extensions have the same strength. The expected output should be "my_class.AA".

If you want to test with different cases, you can modify the arguments of the StrongestExtension method call in the Main class.

Also, make sure to test with different cases to cover all possible scenarios of the problem.
*/

// Note: This solution assumes that the input list of extensions