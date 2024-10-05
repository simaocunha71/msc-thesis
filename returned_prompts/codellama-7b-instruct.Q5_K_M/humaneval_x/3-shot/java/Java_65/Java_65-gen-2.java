        String result = "";
        String digits = String.valueOf(x);
        int num_digits = digits.length();

        shift = shift % num_digits;

        if (shift == 0) {
            return digits;
        } else if (shift > num_digits / 2) {
            shift = num_digits - shift;
        }

        for (int i = 0; i < num_digits; i++) {
            if (i >= shift) {
                result += digits.charAt(i);
            } else {
                result += digits.charAt(i + shift);
            }
        }
        return result;
    }
}

