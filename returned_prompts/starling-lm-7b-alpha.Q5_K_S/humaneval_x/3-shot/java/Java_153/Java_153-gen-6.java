        Collections.sort(extensions, new Comparator<String>() {
            public int compare(String extension1, String extension2) {
                int cap1 = 0;
                int sm1 = 0;
                for (char c : extension1.toCharArray()) {
                    if (c >= 'A' && c <= 'Z') cap1 += 1;
                    if (c >= 'a' && c <= 'z') sm1 += 1;
                }
                int strength1 = cap1 - sm1;

                int cap2 = 0;
                int sm2 = 0;
                for (char c : extension2.toCharArray()) {
                    if (c >= 'A' && c <= 'Z') cap2 += 1;
                    if (c >= 'a' && c <= 'z') sm2 += 1;
                }
                int strength2 = cap2 - sm2;

                return strength1 - strength2;
            }
        });
        return class_name + "." + extensions.get(0);
    }
}

