        String x_str = String.valueOf(x);
        int len = x_str.length();

        if  (shift >= len) return new StringBuilder(x_str).reverse().toString();

        String shifted = x_str.substring(len - shift) + x_str.substring(0, len - shift);
        return shifted;
     }
}

