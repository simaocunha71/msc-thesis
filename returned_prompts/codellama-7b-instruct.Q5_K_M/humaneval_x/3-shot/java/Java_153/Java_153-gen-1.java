        Map<String, Integer> extension_strength = new HashMap<>();
        for (String extension : extensions) {
            int strength = 0;
            int uppercase_count = 0;
            for (char c : extension.toCharArray()) {
                if (Character.isUpperCase(c)) uppercase_count += 1;
                else strength -= 1;
            }
            strength += uppercase_count;
            extension_strength.put(extension, strength);
        }
        String strongest_extension = "";
        int strongest_strength = 0;
        for (String extension : extension_strength.keySet()) {
            int strength = extension_strength.get(extension);
            if (strength > strongest_strength) {
                strongest_strength = strength;
                strongest_extension = extension;
            }
        }
        return class_name + "." + strongest_extension;
    }
}

