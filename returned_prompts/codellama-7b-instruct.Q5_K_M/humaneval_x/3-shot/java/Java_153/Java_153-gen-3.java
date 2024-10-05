        if (extensions.isEmpty()) return class_name;

        String strongest = extensions.get(0);
        int strongest_strength = strength(strongest);

        for (String extension : extensions) {
            int strength = strength(extension);
            if (strength > strongest_strength) {
                strongest = extension;
                strongest_strength = strength;
            } else if (strength == strongest_strength &&
                    (extensions.indexOf(extension) < extensions.indexOf(strongest))) {
                strongest = extension;
                strongest_strength = strength;
            }
        }
        return class_name + "." + strongest;
    }

    private int strength(String extension) {
        int strength = 0;
        for (char c : extension.toCharArray()) {
            if (c >= 'A' && c <= 'Z') strength += c - 'A' + 1;
        }
        strength -= extension.length() - countLowercase(extension);
        return strength;
    }

    private int countLowercase(String extension) {
        int count = 0;
        for (char c : extension.toCharArray()) {
            if (c >= 'a' && c <= 'z') count += 1;
        }
        return count;
    }
}

