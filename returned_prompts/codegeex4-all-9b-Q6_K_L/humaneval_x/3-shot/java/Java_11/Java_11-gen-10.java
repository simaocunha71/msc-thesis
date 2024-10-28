        StringBuilder result = new StringBuilder();

        for (int i = 0; i < Math.max(a.length(), b.length()); i++) {
            int a_val = (i < a.length() && a.charAt(i) == '1') ? 1 : 0;
            int b_val = (i < b.length() && b.charAt(i) == '1') ? 1 : 0;
            result.append(a_val ^ b_val);
        }

        return result.toString();
    }
}

