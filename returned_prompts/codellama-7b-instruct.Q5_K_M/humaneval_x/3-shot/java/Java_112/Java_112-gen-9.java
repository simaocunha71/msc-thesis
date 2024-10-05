        List<Object> result = new ArrayList<>();
        StringBuilder s_result = new StringBuilder();
        boolean is_palindrome = true;

        for (int i = 0; i < s.length(); i++) {
            if (c.indexOf(s.charAt(i)) == -1) {
                s_result.append(s.charAt(i));
            } else {
                is_palindrome = false;
            }
        }

        result.add(s_result.toString());
        result.add(is_palindrome);
        return result;
    }
}

