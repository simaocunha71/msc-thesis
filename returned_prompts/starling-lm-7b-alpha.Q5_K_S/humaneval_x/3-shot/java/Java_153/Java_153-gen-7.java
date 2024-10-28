        double max_strength = Integer.MIN_VALUE;
        String strongest_extension = "";

        for (String extension : extensions) {
            int cap_count = 0;
            int sm_count = 0;

            for (char c : extension.toCharArray()) {
                if (Character.isUpperCase(c)) cap_count += 1;
                if (Character.isLowerCase(c)) sm_count += 1;
            }

            double strength = (cap_count - sm_count);

            if (strength > max_strength) {
                max_strength = strength;
                strongest_extension = extension;
            } else if (strength == max_strength && extension.compareTo(strongest_extension) < 0) {
                strongest_extension = extension;
            }
        }
        return class_name + "." + strongest_extension;
    }
}


