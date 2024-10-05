        int result = 0;
        for (char c : s.toLowerCase().toCharArray()) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || (c == 'y' && s.length() == 1)) {
                result += 1;
            }
        }
        return result;
    }
}

