        for (int i = 0; i < extensions.size(); i++) {
            int cap = 0;
            int sm = 0;
            for (int j = 0; j < extensions.get(i).length(); j++) {
                if (Character.isUpperCase(extensions.get(i).charAt(j))) {
                    cap += 1;
                } else {
                    sm += 1;
                }
            }
            if (cap - sm < 0) {
                continue;
            }
            if (cap - sm < class_name.length()) {
                class_name = class_name + "." + extensions.get(i);
            }
        }
        return class_name;
    }
}

