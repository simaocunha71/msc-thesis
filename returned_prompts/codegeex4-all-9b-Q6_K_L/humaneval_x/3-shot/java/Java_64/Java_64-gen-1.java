        s = s.toLowerCase();
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                count += 1;
            }
        }
        if (s.charAt(s.length() - 1) == 'y') {
            count += 1;
        }
        return count;
    }
}

