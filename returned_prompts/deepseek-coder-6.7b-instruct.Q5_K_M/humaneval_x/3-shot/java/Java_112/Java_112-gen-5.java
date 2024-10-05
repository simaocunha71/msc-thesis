        StringBuilder sb = new StringBuilder();
        Set<Character> set = new HashSet<>();
        for (char ch : c.toCharArray()) {
            set.add(ch);
        }
        for (char ch : s.toCharArray()) {
            if (!set.contains(ch)) {
                sb.append(ch);
            }
        }
        String res = sb.toString();
        boolean isPalindrome = res.equals(new StringBuilder(res).reverse().toString());
        return Arrays.asList(res, isPalindrome);
    }
}

