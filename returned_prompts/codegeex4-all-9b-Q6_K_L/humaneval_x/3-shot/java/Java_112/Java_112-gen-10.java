        StringBuilder sb = new StringBuilder();

        for (char c1 : s.toCharArray()) {
            if (c.indexOf(c1) == -1) {
                sb.append(c1);
            }
        }

        String result = sb.toString();
        boolean isPalindrome = result.equals(new StringBuilder(result).reverse().toString());

        return Arrays.asList(result, isPalindrome);
    }
}

