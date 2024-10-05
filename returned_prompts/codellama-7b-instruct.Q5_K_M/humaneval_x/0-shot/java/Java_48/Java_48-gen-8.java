        // Check for empty string
        if (text.isEmpty()) return true;

        // Check for odd length string
        int len = text.length();
        if (len % 2 == 1) return false;

        // Check for palindrome
        int mid = len / 2;
        for (int i = 0; i < mid; i++) {
            char c1 = text.charAt(i);
            char c2 = text.charAt(len - 1 - i);
            if (c1 != c2) return false;
        }

        return true;
    }
}