        Map<String, Double> extension_strength = new HashMap<>();
        for (String extension : extensions) {
            int cap = 0;
            int sm = 0;
            for (char c : extension.toCharArray()) {
                if (Character.isUpperCase(c)) {
                    cap += 1;
                } else {
                    sm += 1;
                }
            }
            extension_strength.put(extension, (double) cap - sm);
        }
        double max_strength = -1;
        String best_extension = "";
        for (String extension : extensions) {
            double strength = extension_strength.get(extension);
            if (strength > max_strength) {
                max_strength = strength;
                best_extension = extension;
            }
        }
        return class_name + "." + best_extension;
    }
}

