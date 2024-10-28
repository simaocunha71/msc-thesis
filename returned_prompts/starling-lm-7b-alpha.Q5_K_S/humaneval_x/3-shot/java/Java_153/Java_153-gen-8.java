        double max_strength = -1;
        String max_extension = "";
        for (String extension : extensions) {
            int cap_count = 0;
            int sm_count = 0;

            for (int i = 0; i < extension.length(); i++) {
                if (Character.isUpperCase(extension.charAt(i))) {
                    cap_count += 1;
                }
                if (Character.isLowerCase(extension.charAt(i))) {
                    sm_count += 1;
                }
            }

            double strength = (cap_count - sm_count);
            if (max_strength < strength) {
                max_strength = strength;
                max_extension = extension;
            } else if (max_strength == strength && max_extension.compareTo(extension) < 0) {
                max_extension = extension;
            }
        }

        return class_name + "." + max_extension;
    }
}

