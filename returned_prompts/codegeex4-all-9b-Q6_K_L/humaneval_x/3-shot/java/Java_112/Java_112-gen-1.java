        String result = "";
        for (char ch : s.toCharArray()) {
            if (!c.contains(String.valueOf(ch))) {
                result += ch;
            }
        }
        if (result.equals(new StringBuilder(result).reverse().toString())) {
            return Arrays.asList(result, true);
        } else {
            return Arrays.asList(result, false);
        }
    }
}

