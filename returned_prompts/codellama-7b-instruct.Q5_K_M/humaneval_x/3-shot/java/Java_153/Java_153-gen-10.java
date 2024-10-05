        int max_strength = Integer.MIN_VALUE;
        String max_extension = null;

        for (String extension : extensions) {
            int strength = 0;
            for (char c : extension.toCharArray()) {
                if (Character.isUpperCase(c)) strength += 1;
                else strength -= 1;
            }

            if (strength > max_strength) {
                max_strength = strength;
                max_extension = extension;
            } else if (strength == max_strength) {
                if (extensions.indexOf(max_extension) > extensions.indexOf(extension)) {
                    max_strength = strength;
                    max_extension = extension;
                }
            }
        }

        return class_name + "." + max_extension;
    }
}

