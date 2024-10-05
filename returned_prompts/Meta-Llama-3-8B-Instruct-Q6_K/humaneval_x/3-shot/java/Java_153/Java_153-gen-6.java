        String strongest_extension = "";
        double strongest_strength = 0;

        for (String extension : extensions) {
            int cap = 0;
            int sm = 0;
            for (char c : extension.toCharArray()) {
                if (Character.isUpperCase(c)) {
                    cap++;
                } else if (Character.isLowerCase(c)) {
                    sm++;
                }
            }
            double strength = cap - (double) sm;
            if (strength > strongest_strength) {
                strongest_extension = extension;
                strongest_strength = strength;
            }
        }
        return class_name + "." + strongest_extension;
    }
}