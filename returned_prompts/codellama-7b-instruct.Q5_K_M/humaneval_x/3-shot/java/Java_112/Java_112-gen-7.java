        List<Object> result = new ArrayList<>();
        String result_string = "";
        boolean is_palindrome = false;

        for (char sc : s.toCharArray()) {
            if (!c.contains(String.valueOf(sc))) {
                result_string += sc;
            }
        }
        String reversed = new StringBuilder(result_string).reverse().toString();
        if (result_string.equals(reversed)) {
            is_palindrome = true;
        }
        result.add(result_string);
        result.add(is_palindrome);
        return result;

    }
}

