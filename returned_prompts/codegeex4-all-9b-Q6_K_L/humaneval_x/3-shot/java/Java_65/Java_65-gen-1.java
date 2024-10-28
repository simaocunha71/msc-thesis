        String s = String.valueOf(x);
        if (shift > s.length()) {
            return new StringBuilder(s).reverse().toString();
        }
        return s.substring(shift) + s.substring(0, shift);
    }
}

