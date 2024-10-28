        String res = "";
        int strongest = -1;
        for (String ext : extensions) {
            int cap = 0;
            int sm = 0;
            for (char c : ext.toCharArray()) {
                if (Character.isUpperCase(c)) {
                    cap++;
                } else if (Character.isLowerCase(c)) {
                    sm++;
                }
            }
            int strength = cap - sm;
            if (strength > strongest) {
                res = class_name + "." + ext;
                strongest = strength;
            } else if (strength == strongest) {
                res = class_name + "." + ext;
                break A;
            }
        }
        return res;
    }
}

