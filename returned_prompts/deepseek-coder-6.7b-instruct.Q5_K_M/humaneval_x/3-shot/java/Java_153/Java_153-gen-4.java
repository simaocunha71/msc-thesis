        int max_strength = Integer.MIN_VALUE;
        String strongest_extension = "";

        for  (String extension : extensions) {
            int strength = 0;
            for  (char c : extension.toCharArray()) {
                if  (Character.isUpperCase(c)) {
                    strength++;
                } else if  (Character.isLowerCase(c)) {
                    strength--;
                }
            }
            if  (strength > max_strength) {
                max_strength = strength;
                strongest_extension = extension;
            }
        }
        return class_name + "." + strongest_extension;
     }
}

