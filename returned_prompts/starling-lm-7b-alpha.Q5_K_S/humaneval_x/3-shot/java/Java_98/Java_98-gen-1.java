        int count = 0;
        for (int i = 0; i < s.length(); i += 2) {
            if (s.charAt(i) >= 'A' && s.charAt(i) <= 'Z') {
                count += 1;
            }
        }
        return count;
    }
}

