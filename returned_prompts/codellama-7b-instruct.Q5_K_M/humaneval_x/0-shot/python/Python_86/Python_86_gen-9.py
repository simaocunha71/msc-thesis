        int max = 0, i = 0;
        for (String s : extensions) {
            int cap = 0, sm = 0;
            for (int j = 0; j < s.length(); j++) {
                if (Character.isUpperCase(s.charAt(j))) {
                    cap++;
                } else {
                    sm++;
                }
            }
            int strength = cap - sm;
            if (strength > max) {
                max = strength;
                i = extensions.indexOf(s);
            } else if (strength == max && extensions.indexOf(s) < i) {
                i = extensions.indexOf(s);
            }
        }
        return class_name + "." + extensions.get(i);
    }
}
