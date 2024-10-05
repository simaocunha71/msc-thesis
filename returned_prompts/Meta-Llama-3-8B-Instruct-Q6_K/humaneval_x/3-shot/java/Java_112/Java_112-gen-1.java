        String result = "";
        for (char c1 : s.toCharArray()) {
            if (!c.contains(String.valueOf(c1))) {
                result += c1;
            }
        }
        return Arrays.asList(result, result.equals(new StringBuilder(result).reverse().toString()));
    }
}