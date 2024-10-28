        Collections.sort(extensions, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                int cap_count = 0, sm_count = 0, i = 0;
                for (char c : o1.toCharArray()) {
                    if (Character.isUpperCase(c)) {
                        cap_count += 1;
                    } else {
                        sm_count += 1;
                    }
                }
                int cap_count2 = 0, sm_count2 = 0, i2 = 0;
                for (char c : o2.toCharArray()) {
                    if (Character.isUpperCase(c)) {
                        cap_count2 += 1;
                    } else {
                        sm_count2 += 1;
                    }
                }
                int strength1 = cap_count - sm_count;
                int strength2 = cap_count2 - sm_count2;
                if (strength1 != strength2) {
                    return strength1 - strength2;
                } else {
                    return i - i2;
                }
            }
        });
        return class_name + "." + extensions.get(0);
    }
}




```