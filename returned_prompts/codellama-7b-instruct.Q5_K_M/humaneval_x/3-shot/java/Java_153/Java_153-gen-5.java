        int strongest = 0, strongest_index = 0;
        for (int i = 0; i < extensions.size(); i++) {
            int strength = 0;
            for (int j = 0; j < extensions.get(i).length(); j++) {
                if (Character.isUpperCase(extensions.get(i).charAt(j))) {
                    strength += 1;
                } else {
                    strength -= 1;
                }
            }
            if (strength > strongest) {
                strongest = strength;
                strongest_index = i;
            }
        }
        return class_name + "." + extensions.get(strongest_index);
    }
}

