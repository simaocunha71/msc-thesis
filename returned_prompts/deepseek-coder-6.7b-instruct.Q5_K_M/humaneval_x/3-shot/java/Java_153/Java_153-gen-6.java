        double maxStrength = - Double.MAX_VALUE;
        String maxExtension = "";

        for (String extension : extensions) {
            double strength = getStrength(extension);
            if (strength > maxStrength) {
                maxStrength = strength;
                maxExtension = extension;
            }
        }

        return class_name + "." + maxExtension;
    }

    private double getStrength(String extension) {
        int upperCase = 0;
        int lowerCase = 0;

        for (char c : extension.toCharArray()) {
            if (Character.isUpperCase(c)) {
                upperCase++;
            } else if (Character.isLowerCase(c)) {
                lowerCase++;
            }
        }

        return upperCase - lowerCase;
    }
}

