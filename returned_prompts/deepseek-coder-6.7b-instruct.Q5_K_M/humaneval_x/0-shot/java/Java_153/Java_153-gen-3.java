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

This is a Java solution for the problem. The function "StrongestExtension" calculates the strength of each extension by subtracting the number of lowercase characters from the number of uppercase characters. The extension with the highest strength is then returned. If there are multiple extensions with the same strength, the one that comes first in the list is returned. The function "countUpperCase" and "countLowerCase" are helper functions that count the number of uppercase and lowercase characters in a string, respectively.
