        String strongest_extension = null;
        int strongest_strength = Integer.MIN_VALUE;

        for (String extension : extensions) {
            int uppercase_count = 0;
            int lowercase_count = 0;

            for (char c : extension.toCharArray()) {
                if (Character.isUpperCase(c)) {
                    uppercase_count += 1;
                } else if (Character.isLowerCase(c)) {
                    lowercase_count += 1;
                }
            }

            int strength = uppercase_count - lowercase_count;

            if (strength > strongest_strength) {
                strongest_extension = extension;
                strongest_strength = strength;
            }
        }

        return class_name + "." + strongest_extension;
    }
}

