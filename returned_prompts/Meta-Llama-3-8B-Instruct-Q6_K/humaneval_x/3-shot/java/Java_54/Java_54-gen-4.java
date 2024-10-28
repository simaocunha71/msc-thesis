        if (s0.length() != s1.length()) {
            return false;
        }
        Arrays.sort(s0.toCharArray());
        Arrays.sort(s1.toCharArray());
        return Arrays.equals(s0.toCharArray(), s1.toCharArray());
    }
}

