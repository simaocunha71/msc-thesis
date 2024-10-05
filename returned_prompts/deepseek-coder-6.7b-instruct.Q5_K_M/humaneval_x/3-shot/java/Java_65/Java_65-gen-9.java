        String str_x = Integer.toString(x);
        int n = str_x.length();

        if (shift >= n) {
            return new StringBuilder(str_x).reverse().toString();
        }

        return str_x.substring(n - shift) + str_x.substring(0, n - shift);
    }
}

