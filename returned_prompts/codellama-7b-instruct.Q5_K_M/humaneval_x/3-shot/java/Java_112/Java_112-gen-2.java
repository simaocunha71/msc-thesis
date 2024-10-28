        List<Object> result = new ArrayList<>();
        StringBuilder result_string = new StringBuilder();
        boolean is_palindrome = true;

        for (char s_char : s.toCharArray()) {
            if (!c.contains(s_char + "")) {
                result_string.append(s_char);
            } else {
                is_palindrome = false;
            }
        }

        result.add(result_string.toString());
        result.add(is_palindrome);

        return result;
    }
}

