        int maxStrength = Integer.MIN_VALUE;
        String strongestExtension = "";

        for(String ext : extensions) {
            int strength = 0;
            for(char c : ext.toCharArray()) {
                if(Character.isUpperCase(c)) {
                    strength++;
                } else if(Character.isLowerCase(c)) {
                    strength--;
                }
            }

            if(strength > maxStrength) {
                maxStrength = strength;
                strongestExtension = ext;
            }
        }

        return class_name + "." + strongestExtension;
    }
}

