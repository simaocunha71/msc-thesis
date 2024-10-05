        double max_strength = -1;
        String max_extension = "";
        for (String extension : extensions) {
            double strength = 0;
            for (char c : extension.toCharArray()) {
                if (Character.isUpperCase(c)) strength += 1;
                if (Character.isLowerCase(c)) strength -= 1;
            }
            if (strength > max_strength) {
                max_strength = strength;
                max_extension = extension;
            }
        }
        return class_name + "." + max_extension;
    }
}

