        String result = class_name + ".";
        double max_strength = 0;
        String max_extension = "";

        for (String extension : extensions) {
            int cap_count = 0;
            int sm_count = 0;

            for (int i = 0; i < extension.length(); i++) {
                if (Character.isUpperCase(extension.charAt(i))) {
                    cap_count += 1;
                } else {
                    sm_count += 1;
                }
            }

            double strength = (cap_count - sm_count) / (double) extension.length();

            if (strength >= max_strength) {
                max_strength = strength;
                max_extension = extension;
            }
        }

        return result + max_extension;
    }
}


```