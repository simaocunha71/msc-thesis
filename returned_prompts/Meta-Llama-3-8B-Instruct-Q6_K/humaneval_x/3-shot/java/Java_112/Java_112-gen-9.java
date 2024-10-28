        List<Object> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        boolean isPalindrome = true;

        for (char c_s : s.toCharArray()) {
            boolean isPresent = false;
            for (char c_c : c.toCharArray()) {
                if (c_s == c_c) {
                    isPresent = true;
                    break;
                }
            }
            if (!isPresent) {
                sb.append(c_s);
            } else {
                isPalindrome = false;
            }
        }
        result.add(sb.toString());
        result.add(isPalindrome);
        return result;
    }
}