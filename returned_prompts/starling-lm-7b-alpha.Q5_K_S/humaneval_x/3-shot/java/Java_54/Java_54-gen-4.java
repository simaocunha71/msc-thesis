        if (s0.length() != s1.length()) return false;
        if (s0.equals(s1)) return true;

        char[] chars0 = s0.toCharArray();
        char[] chars1 = s1.toCharArray();

        Arrays.sort(chars0);
        Arrays.sort(chars1);

        return Arrays.equals(chars0, chars1);
    }
}

