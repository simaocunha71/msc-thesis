        int result = 0;
        for (char c : s.toCharArray()) {
            if (c >= 'A' && c <= 'Z') {
                result += c;
            }
        }
        return result;
    }
}

