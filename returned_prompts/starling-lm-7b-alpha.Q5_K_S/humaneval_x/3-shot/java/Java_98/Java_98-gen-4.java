        int count = 0;
        String upper_vowels = "ABCDE";
        for (int i = 0; i < s.length(); i += 2) {
            char c = s.charAt(i);
            if (upper_vowels.indexOf(c) != -1) {
                count += 1;
            }
        }
        return count;
    }
}

