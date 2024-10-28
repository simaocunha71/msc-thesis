        String str = String.valueOf(x);
        if (shift >= str.length()) {
            return new StringBuilder(str).reverse().toString();
        } else {
            return str.substring(str.length() - shift) + str.substring(0, str.length() - shift);
        }
    }
}

