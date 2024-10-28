        StringBuilder result = new StringBuilder();
        int digits = 0;
        int digit = x;
        while (digit > 0) {
            digit /= 10;
            digits += 1;
        }
        while (digits > 0) {
            digit = x % 10;
            x /= 10;
            result.append(String.valueOf(digit));
            digits -= 1;
        }
        if (shift >= result.length()) {
            shift = result.length() - shift;
            result.reverse();
            return result.toString();
        }
        result.deleteCharAt(result.length() - shift);
        return result.toString();
    }
}

