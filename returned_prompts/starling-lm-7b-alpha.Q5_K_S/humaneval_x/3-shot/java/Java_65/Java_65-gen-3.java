        StringBuilder result = new StringBuilder();
        int digits = 0;
        int y = x;
        while (y > 0) {
            digits += 1;
            y /= 10;
        }
        while (shift > digits) {
            shift -= digits;
        }
        while (x > 0) {
            int digit = x % 10;
            result.append(String.valueOf(digit));
            x /= 10;
        }
        while (shift > 0) {
            int digit = x % 10;
            result.append(String.valueOf(digit));
            shift -= 1;
            x /= 10;
        }
        return result.toString();
    }
}

