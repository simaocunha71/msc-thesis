        String digits = Integer.toString(x);
        shift = shift % digits.length();
        if (shift == 0) return digits;
        return digits.substring(digits.length() - shift) + digits.substring(0, digits.length() - shift);
    }
}

