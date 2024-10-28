        int max_strength = -1;
        String strongest_extension = null;

        for (String extension : extensions) {
            int cap = 0, sm = 0;
            for (char c : extension.toCharArray()) {
                if (Character.isUpperCase(c)) cap++;
                else sm++;
            }
            int strength = cap - sm;
            if (strength > max_strength) {
                max_strength = strength;
                strongest_extension = extension;
            }
        }
        return class_name + "." + strongest_extension;
    }
}

