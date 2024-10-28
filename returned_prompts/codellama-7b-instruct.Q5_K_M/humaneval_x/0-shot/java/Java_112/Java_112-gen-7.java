        List<Object> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        boolean isPalindrome = false;

        for (int i = 0; i < s.length(); i++) {
            if (c.indexOf(s.charAt(i)) != -1) {
                continue;
            } else {
                sb.append(s.charAt(i));
            }
        }

        for (int i = 0; i < sb.length() / 2; i++) {
            if (sb.charAt(i) != sb.charAt(sb.length() - 1 - i)) {
                isPalindrome = false;
                break;
            } else {
                isPalindrome = true;
            }
        }
        result.add(sb.toString());
        result.add(isPalindrome);

        return result;
    }
}


