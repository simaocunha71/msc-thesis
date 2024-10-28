        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (c.indexOf(s.charAt(i)) == -1) {
                sb.append(s.charAt(i));
            }
        }
        String result = sb.toString();
        return Arrays.asList(result, result.equals(new StringBuilder(result).reverse().toString()));
    }
}

