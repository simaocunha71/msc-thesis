        List<Object> result = new ArrayList<>();
        result.add(0, "");
        result.add(1, false);

        for (char s_char : s.toCharArray()) {
            boolean is_match = false;
            for (char c_char : c.toCharArray()) {
                if (s_char == c_char) {
                    is_match = true;
                    break;
                }
            }
            if (!is_match) result.get(0) += s_char;
        }

        String result_string = result.get(0).toString();
        result.set(0, result_string);
        result.set(1, isPalindrome(result_string));
        return result;
    }

    public boolean isPalindrome(String str) {
        String reverse_string = new StringBuilder(str).reverse().toString();
        if (reverse_string.equals(str)) return true;
        else return false;
    }
}

