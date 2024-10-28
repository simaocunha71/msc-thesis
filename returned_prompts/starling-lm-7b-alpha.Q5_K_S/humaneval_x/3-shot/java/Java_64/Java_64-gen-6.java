        int vowels = 0;
        String vowels_str = "aeiouy";
        for (int i = 0; i < s.length(); i++) {
            if (vowels_str.contains(s.substring(i, i + 1))) {
                vowels += 1;
            }
        }
        return vowels;
    }
}

