        String s = String.valueOf(x);
        if (shift >= s.length()) return new StringBuilder(s).reverse().toString();

        StringBuilder result = new StringBuilder();
        for (int i = shift; i < s.length(); i++) {
            result.append(s.charAt(i));
        }
        for (int i = 0; i < shift; i++) {
            result.append(s.charAt(i));
        }
        return result.toString();
    }
}

