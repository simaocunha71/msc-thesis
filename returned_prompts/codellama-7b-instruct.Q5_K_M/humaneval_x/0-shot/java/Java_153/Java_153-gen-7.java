        int strongestStrength = 0;
        String strongestExtension = "";
        for (String extension: extensions) {
            int cap = 0;
            int sm = 0;
            for (int i = 0; i < extension.length(); i++) {
                char c = extension.charAt(i);
                if (Character.isUpperCase(c)) {
                    cap++;
                } else if (Character.isLowerCase(c)) {
                    sm++;
                }
            }
            int strength = cap - sm;
            if (strength > strongestStrength) {
                strongestStrength = strength;
                strongestExtension = extension;
            }
        }
        return class_name + "." + strongestExtension;
    }
}
