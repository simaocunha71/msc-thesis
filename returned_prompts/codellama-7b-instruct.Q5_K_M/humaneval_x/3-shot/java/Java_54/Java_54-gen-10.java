        if (s0.length() != s1.length()) return false;

        char[] c0 = s0.toCharArray();
        char[] c1 = s1.toCharArray();

        Arrays.sort(c0);
        Arrays.sort(c1);

        for (int i = 0; i < c0.length; i++) {
            if (c0[i] != c1[i]) return false;
        }
        return true;
    }
}

