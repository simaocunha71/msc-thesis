        String result = class_name + ".";
        double max_strength = 0;
        for (String ext : extensions) {
            double strength = 0;
            for (char c : ext.toCharArray()) {
                if (c >= 'A' && c <= 'Z') strength += 1;
                if (c >= 'a' && c <= 'z') strength -= 1;
            }
            if (strength > max_strength) {
                max_strength = strength;
                result = class_name + "." + ext;
            }
        }
        return result;
    }
}

