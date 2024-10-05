        String max = "", maxStr = "";
        int maxStrStrength = 0;

        for (String extension : extensions) {
            int strength = 0;
            int count = 0;
            for (int i = 0; i < extension.length(); i++) {
                if (Character.isUpperCase(extension.charAt(i))) {
                    strength += 1;
                } else if (Character.isLowerCase(extension.charAt(i))) {
                    strength -= 1;
                }
            }

            if (strength > maxStrStrength) {
                max = class_name + "." + extension;
                maxStrStrength = strength;
            }
        }

        return max;
    }
}




/*
    class Solution {
    public String StrongestExtension(String class_name, List<String> extensions) {
        String max = "", maxStr = "";
        int maxStrStrength = 0;

        for (String extension : extensions) {
            int strength = 0;
            for (int i = 0; i < extension.length(); i++) {
                if (Character.isUpperCase(extension.charAt(i))) {
                    strength += 1;
                } else if (Character.isLowerCase(extension.charAt(i))) {
                    strength -= 1;
                }
            }

            if (strength > maxStrStrength) {
                max = class_name + "." + extension;
                maxStrStrength = strength;
            }
        }

        return max;
    }
}
*/







*/
```