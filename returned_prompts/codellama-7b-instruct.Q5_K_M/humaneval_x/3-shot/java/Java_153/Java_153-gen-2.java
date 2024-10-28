        if (extensions.size() == 0) return class_name;

        String strongest_extension = extensions.get(0);
        double strongest_strength = -1;
        for (String extension : extensions) {
            double strength = 0;
            for (char c : extension.toCharArray()) {
                if (Character.isUpperCase(c)) {
                    strength -= 1;
                } else {
                    strength += 1;
                }
            }
            if (strength > strongest_strength) {
                strongest_strength = strength;
                strongest_extension = extension;
            } else if (strength == strongest_strength) {
                if (extensions.indexOf(strongest_extension) > extensions.indexOf(extension)) {
                    strongest_extension = extension;
                }
            }
        }
        return class_name + "." + strongest_extension;
    }
}

