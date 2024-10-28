        String result = "";

        // Get digits of x
        String str_x = String.valueOf(x);
        char[] digits = str_x.toCharArray();

        // Calculate number of digits
        int num_digits = digits.length;

        // Calculate shift amount
        int final_shift = shift % num_digits;

        // Shift digits
        for (int i = 0; i < num_digits; i++) {
            if (final_shift == 0) {
                result += digits[i];
            } else if (final_shift == num_digits) {
                result = digits[i] + result;
            } else {
                if (i < final_shift) {
                    result = digits[i] + result;
                } else {
                    result += digits[i];
                }
            }
        }
        return result;
    }
}

