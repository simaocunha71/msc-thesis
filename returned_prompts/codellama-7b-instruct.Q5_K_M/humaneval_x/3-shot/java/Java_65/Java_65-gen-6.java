        if (x < 0 || shift < 0) return null;

        String x_str = String.valueOf(x);
        int n_digits = x_str.length();
        int shift_abs = Math.abs(shift);

        if (shift_abs > n_digits) return new StringBuilder(x_str).reverse().toString();

        String shifted = x_str.substring(shift_abs) + x_str.substring(0, shift_abs);
        return shifted;
    }
}

