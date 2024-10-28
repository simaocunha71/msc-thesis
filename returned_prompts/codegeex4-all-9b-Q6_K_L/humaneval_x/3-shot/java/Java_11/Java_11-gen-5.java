        StringBuilder result = new StringBuilder();

        for (int i = 0; i < Math.max(a.length(), b.length()); i++) {
            char a_bit = i < a.length() ? a.charAt(i) : '0';
            char b_bit = i < b.length() ? b.charAt(i) : '0';
            result.append((a_bit ^ b_bit) == '1' ? '1' : '0');
        }
        return result.toString();
    }
}

