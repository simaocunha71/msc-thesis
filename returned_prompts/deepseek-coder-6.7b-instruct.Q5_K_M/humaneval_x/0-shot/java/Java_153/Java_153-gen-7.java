        int maxStrength = Integer.MIN_VALUE;
        String strongestExtension = "";

        for (String extension : extensions) {
            int strength = countUpperCase(extension) - countLowerCase(extension);
            if (strength > maxStrength) {
                maxStrength = strength;
                strongestExtension = extension;
            }
        }

        return class_name + "." + strongestExtension;
    }

    private int countUpperCase(String str) {
        int count = 0;
        for (char c : str.toCharArray()) {
            if (Character.isUpperCase(c)) {
                count++;
            }
        }
        return count;
    }

    private int countLowerCase(String str) {
        int count = 0;
        for (char c : str.toCharArray()) {
            if (Character.isLowerCase(c)) {
                count++;
            }
        }
        return count;
    }
}

//  The time complexity of this solution is O(n*m), where n is the number of extensions and m is the length of each extension.
//  The space complexity is O(1), since no additional space is used.

This solution works by iterating over each extension in the list, calculating its strength, and then comparing it to the current maximum strength. If the extension's strength is greater, it becomes the new maximum strength and the corresponding extension name is stored. Finally, the class name and the strongest extension name are concatenated and returned.

The helper methods countUpperCase and countLowerCase are used to count the number of uppercase and lowercase letters in the extension names, respectively. This information is used to calculate the strength of each extension.
*/

//  Test cases
//  System.out.println(s.StrongestExtension("my_class", Arrays.asList(new String[] {"AA", "Be", "CC"})));  // "my_class.AA"
//  System.out.println(s.StrongestExtension("Slices", Arrays.asList(new String[] {"SErviNGSliCes", "Cheese", "StuFfed"})));  // "S