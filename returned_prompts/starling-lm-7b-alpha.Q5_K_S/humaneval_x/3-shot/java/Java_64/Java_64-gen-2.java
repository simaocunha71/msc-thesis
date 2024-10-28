        int result = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || (c == 'y' && i == s.length() - 1)) {
                result += 1;
            }
        }
        return result;
    }
}

