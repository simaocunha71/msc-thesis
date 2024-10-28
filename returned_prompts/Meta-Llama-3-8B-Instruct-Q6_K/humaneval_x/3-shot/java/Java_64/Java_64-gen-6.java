        int count = 0;
        for (char c : s.toLowerCase().toCharArray()) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                count++;
            } else if (c == 'y' && s.length() - 1 == s.indexOf(c)) {
                count++;
            }
        }
        return count;
    }
}

