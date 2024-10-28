        int count = 0;
        boolean result = false;

        for (char c : string.toCharArray()) {
            if (c == '[') {
                count += 1;
                result = true;
            } else if (c == ']') {
                count -= 1;
                if (count < 0) return false;
            }
        }
        return result && count == 0;
    }
}

