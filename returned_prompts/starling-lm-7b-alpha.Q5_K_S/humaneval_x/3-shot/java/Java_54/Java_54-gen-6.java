        char[] s0_chars = s0.toCharArray();
        char[] s1_chars = s1.toCharArray();

        Arrays.sort(s0_chars);
        Arrays.sort(s1_chars);

        return Arrays.equals(s0_chars, s1_chars);
    }
}

