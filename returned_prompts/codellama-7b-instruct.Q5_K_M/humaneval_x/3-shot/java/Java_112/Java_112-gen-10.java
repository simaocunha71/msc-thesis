        List<Object> result = new ArrayList<>();
        String result_string = "";
        boolean is_palindrome = true;

        for (int i = 0; i < s.length(); i++) {
            if (!c.contains(s.substring(i, i + 1))) {
                result_string += s.substring(i, i + 1);
            } else {
                is_palindrome = false;
            }
        }
        result.add(result_string);
        result.add(is_palindrome);
        return result;
    }
}

