        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || (c == 'y' && s.length() > 0 && (s.charAt(s.length() - 1) == 'a' || s.charAt(s.length() - 1) == 'e' || s.charAt(s.length() - 1) == 'i' || s.charAt(s.length() - 1) == 'o' || s.charAt(s.length() - 1) == 'u'))) {
                count += 1;
            }
        }
        return count;
    }
}

