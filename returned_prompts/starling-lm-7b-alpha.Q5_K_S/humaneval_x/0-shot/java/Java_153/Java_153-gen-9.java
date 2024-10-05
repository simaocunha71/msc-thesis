    int max = Integer.MIN_VALUE;
    int idx = 0;
    for (int i = 0; i < extensions.size(); i++) {
        String ext = extensions.get(i);
        int cap = 0;
        int small = 0;
        for (int j = 0; j < ext.length(); j++) {
            if (Character.isUpperCase(ext.charAt(j))) {
                cap++;
            } else {
                small++;
            }
        }
        int strength = cap - small;
        if (strength > max) {
            max = strength;
            idx = i;
        } else if (strength == max) {
            if (cap < extensions.get(idx).length() - small) {
                max = strength;
                idx = i;
            }
        }
    }
    return class_name + "." + extensions.get(idx);


















