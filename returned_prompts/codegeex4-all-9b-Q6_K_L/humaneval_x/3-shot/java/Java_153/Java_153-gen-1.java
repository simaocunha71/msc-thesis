        double max_strength = Double.NEGATIVE_INFINITY;
        String max_extension = "";

        for (String extension : extensions) {
            int uppercase = 0, lowercase = 0;
            for (char c : extension.toCharArray()) {
                if (Character.isUpperCase(c)) uppercase += 1;
                else lowercase += 1;
            }

            double strength = uppercase - lowercase;
            if (strength >= max_strength) {
                max_strength = strength;
                max_extension = extension;
            }
        }

        return class_name + "." + max_extension;
    }
}

