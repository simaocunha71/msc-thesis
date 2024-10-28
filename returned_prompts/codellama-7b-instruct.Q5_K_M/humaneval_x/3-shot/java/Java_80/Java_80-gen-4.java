        if (s.length() < 3) return false;
        char[] str = s.toCharArray();
        for (int i = 0; i < str.length - 2; i++) {
            if (str[i] == str[i + 1] && str[i + 1] == str[i + 2]) return false;
        }
        return true;
    }
}

