        String result = class_name + ".";
        double max_strength = Double.NEGATIVE_INFINITY;
        for (String extension : extensions) {
            int cap_count = 0;
            int sm_count = 0;
            for (char c : extension.toCharArray()) {
                if (c >= 'A' && c <= 'Z') {
                    cap_count += 1;
                } else if (c >= 'a' && c <= 'z') {
                    sm_count += 1;
                }
            }
            double strength = (cap_count - sm_count);

            if (strength >= max_strength) {
                max_strength = strength;
                result = class_name + "." + extension;
            }
        }
        return result;
    }
}

