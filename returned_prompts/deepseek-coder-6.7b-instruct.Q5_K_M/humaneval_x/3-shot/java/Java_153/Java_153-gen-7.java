        int maxStrength = Integer.MIN_VALUE;
        String maxExtension = "";

        for (String extension : extensions) {
            int cap = 0, sm = 0;
            for (char c : extension.toCharArray()) {
                if (Character.isUpperCase(c)) {
                    cap++;
                } else if (Character.isLowerCase(c)) {
                    sm++;
                }
            }
            int strength = cap - sm;
            if (strength > maxStrength) {
                maxStrength = strength;
                maxExtension = extension;
            }
        }
        return class_name + "." + maxExtension;
    }
}

