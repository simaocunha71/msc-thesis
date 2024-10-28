        double max_strength = Double.MIN_VALUE;
        String max_extension = "";

        for (String extension : extensions) {
            int cap = 0;
            int sm = 0;
            for (char c : extension.toCharArray()) {
                if (Character.isUpperCase(c)) cap += 1;
                if (Character.isLowerCase(c)) sm += 1;
            }
            double strength = cap - sm;
            if (strength > max_strength) {
                max_strength = strength;
                max_extension = extension;
            }
        }
        return class_name + "." + max_extension;
    }
}

