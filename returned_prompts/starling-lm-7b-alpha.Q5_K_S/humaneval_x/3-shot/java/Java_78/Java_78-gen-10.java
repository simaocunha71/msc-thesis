        int result = 0;
        for (char c : num.toUpperCase().toCharArray()) {
            if (c >= '2' && c <= '9') {
                result += c - '0';
            } else if (c >= 'A' && c <= 'F') {
                result += c - 'A' + 10;
            }
        }
        return result;
    }
}

