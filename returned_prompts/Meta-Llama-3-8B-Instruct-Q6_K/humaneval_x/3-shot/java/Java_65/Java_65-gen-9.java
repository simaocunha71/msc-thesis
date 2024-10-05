        String str = String.valueOf(x);
        int length = str.length();
        if (shift >= length) {
            return new StringBuilder(str).reverse().toString();
        }
        return str.substring(shift) + str.substring(0, shift);
    }
}

