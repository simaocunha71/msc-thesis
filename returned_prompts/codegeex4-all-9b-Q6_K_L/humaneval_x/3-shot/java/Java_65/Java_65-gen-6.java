        String digits = String.valueOf(x);
        return shift > digits.length() ? new StringBuilder(digits).reverse().toString() : digits.substring(shift) + digits.substring(0, shift);
    }
}

