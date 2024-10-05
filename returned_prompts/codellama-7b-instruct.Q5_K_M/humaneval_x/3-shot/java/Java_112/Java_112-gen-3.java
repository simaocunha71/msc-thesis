        List<Object> result = new ArrayList<>();
        StringBuilder result_string = new StringBuilder();
        boolean is_palindrome = true;

        for (char s_char : s.toCharArray()) {
            if (!c.contains(String.valueOf(s_char))) {
                result_string.append(s_char);
            }
        }

        for (int i = 0; i < result_string.length() / 2; i++) {
            if (result_string.charAt(i) != result_string.charAt(result_string.length() - 1 - i)) {
                is_palindrome = false;
                break;
            }
        }

        result.add(result_string.toString());
        result.add(is_palindrome);
        return result;

    }
}

