        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'y') {
                if (s.endsWith("y") && c == 'y') {
                    continue;
                }
                count++;
            }
        }
        return count;
    }
}

