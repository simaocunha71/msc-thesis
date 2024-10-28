        int count = 0;

        for (int i = 0; i < string.length(); i++) {
            if (string.charAt(i) == '[') {
                count += 1;
            } else if (string.charAt(i) == ']') {
                count -= 1;
            }
            if (count < 0) {
                return false;
            }
        }
        return count > 0;
    }
}

