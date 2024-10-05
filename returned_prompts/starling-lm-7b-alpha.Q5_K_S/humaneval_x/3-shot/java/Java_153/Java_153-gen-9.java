        String result = class_name;
        double max_strength = 0;

        for (String extension : extensions) {
            double strength = 0;
            int cap = 0;
            int sm = 0;
            for (char c : extension.toCharArray()) {
                if (Character.isUpperCase(c)) cap += 1;
                if (Character.isLowerCase(c)) sm += 1;
            }
            strength = cap - sm;
            if (strength > max_strength) {
                max_strength = strength;
                result = result + "." + extension;
            }
        }
        return result;
    }
}

