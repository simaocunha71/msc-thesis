        if (extensions.size() == 0) return class_name;
        int class_length = class_name.length();
        int max_length = 0;
        String max_extension = "";
        int max_strength = 0;
        for (String extension : extensions) {
            int extension_length = extension.length();
            if (extension_length > class_length) {
                continue;
            }
            int lower_case = 0;
            int upper_case = 0;
            for (int i = 0; i < extension_length; i++) {
                char c = extension.charAt(i);
                if (c >= 'a' && c <= 'z') {
                    lower_case++;
                } else if (c >= 'A' && c <= 'Z') {
                    upper_case++;
                }
            }
            int strength = upper_case - lower_case;
            if (strength > max_strength) {
                max_strength = strength;
                max_length = extension_length;
                max_extension = extension;
            } else if (strength == max_strength && extension_length < max_length) {
                max_length = extension_length;
                max_extension = extension;
            }
        }
        return class_name + "." + max_extension;
    }
}

