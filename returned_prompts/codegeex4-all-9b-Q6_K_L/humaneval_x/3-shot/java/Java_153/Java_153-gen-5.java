        String strongest = extensions.get(0);
        double max_strength = 0;

        for (String extension : extensions) {
            int CAP = 0;
            int SM = 0;
            for (char c : extension.toCharArray()) {
                if (Character.isUpperCase(c)) CAP += 1;
                else SM += 1;
            }

            double strength = CAP - SM;

            if (strength > max_strength) {
                strongest = extension;
                max_strength = strength;
            }
        }
        return class_name + "." + strongest;
    }
}

