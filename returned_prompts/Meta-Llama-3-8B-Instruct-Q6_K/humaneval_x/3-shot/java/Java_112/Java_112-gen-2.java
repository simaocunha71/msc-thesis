        StringBuilder sb = new StringBuilder();
        for (char c1 : s.toCharArray()) {
            if (!c.contains(String.valueOf(c1))) {
                sb.append(c1);
            }
        }
        String result = sb.toString();
        return Arrays.asList(result, result.equals(new StringBuilder(result).reverse().toString()));
    }
}