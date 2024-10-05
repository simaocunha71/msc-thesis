        int max_strength = Integer.MIN_VALUE;
        String strongest_extension = null;

        for (String extension : extensions) {
            int strength = 0;
            for (char c : extension.toCharArray()) {
                if (Character.isUpperCase(c)) strength += 1;
                else if (Character.isLowerCase(c)) strength -= 1;
            }
            if (strength > max_strength) {
                max_strength = strength;
                strongest_extension = extension;
            }
        }
        return class_name + "." + strongest_extension;
    }
}

