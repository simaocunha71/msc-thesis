        String x_str = Integer.toString(x);
        int length = x_str.length();

        if (shift >= length) {
            return new StringBuilder(x_str).reverse().toString();
        }

        String left = x_str.substring(0, length - shift);
        String right = x_str.substring(length - shift, length);

        return right + left;
     }
}

