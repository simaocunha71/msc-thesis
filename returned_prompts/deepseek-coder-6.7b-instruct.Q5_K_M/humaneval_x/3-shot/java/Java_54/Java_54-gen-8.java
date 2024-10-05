        int[] counts0 = new int[26];
        int[] counts1 = new int[26];

        for (char c : s0.toCharArray()) {
            counts0[c - 'a']++;
        }

        for (char c : s1.toCharArray()) {
            counts1[c - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if (counts0[i] != counts1[i]) {
                return false;
            }
        }

        return true;
    }
}

