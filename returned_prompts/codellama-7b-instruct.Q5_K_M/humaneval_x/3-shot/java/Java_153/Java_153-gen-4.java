        int strongest_extension_strength = 0;
        String strongest_extension_name = "";

        for (String extension : extensions) {
            int CAP = 0;
            int SM = 0;

            for (char c : extension.toCharArray()) {
                if (c >= 'A' && c <= 'Z') CAP += 1;
                if (c >= 'a' && c <= 'z') SM += 1;
            }
            int strength = CAP - SM;

            if (strongest_extension_strength < strength) {
                strongest_extension_strength = strength;
                strongest_extension_name = extension;
            } else if (strongest_extension_strength == strength &&
                    extensions.indexOf(strongest_extension_name) > extensions.indexOf(extension)) {
                strongest_extension_strength = strength;
                strongest_extension_name = extension;
            }
        }

        return class_name + "." + strongest_extension_name;
    }
}

