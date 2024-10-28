        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || (ch == 'y' && i == s.length() - 1)) {
                count++;
            }
        }
        return count;
    }
}

