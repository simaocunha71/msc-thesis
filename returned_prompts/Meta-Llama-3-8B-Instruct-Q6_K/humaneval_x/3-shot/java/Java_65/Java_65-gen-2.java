        String str = String.valueOf(x);
        if (shift >= str.length()) {
            return new StringBuilder(str).reverse().toString();
        }
        return str.substring(shift) + str.substring(0, shift);
    }
}

