        if (s.length() < 3) return false;
        int[] char_set = new int[256];
        Arrays.fill(char_set, 0);
        for (int i = 0; i < 3; i++) {
            char_set[s.charAt(i)] += 1;
        }
        for (int i = 3; i < s.length(); i++) {
            if (char_set[s.charAt(i)] == 1) return false;
            char_set[s.charAt(i)] += 1;
            char_set[s.charAt(i-3)] -= 1;
        }
        return true;

    }
}

