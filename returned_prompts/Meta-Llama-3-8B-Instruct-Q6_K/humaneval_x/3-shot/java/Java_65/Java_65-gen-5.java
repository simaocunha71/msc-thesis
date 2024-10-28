        String s = Integer.toString(x);
        int length = s.length();
        if (shift >= length) {
            return new StringBuilder(s).reverse().toString();
        }
        return s.substring(shift) + s.substring(0, shift);
    }
}

