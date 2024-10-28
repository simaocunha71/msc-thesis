        int count = 0;
        for (char c : s.toLowerCase().toCharArray()) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                count++;
            }
        }
        if (s.charAt(s.length() - 1) == 'y') {
            count++;
        }
        return count;
    }
}

