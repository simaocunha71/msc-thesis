        StringBuilder sb = new StringBuilder();
        boolean isPalindrome = true;

        for (char ch : s.toCharArray()) {
            if (!c.contains(String.valueOf(ch))) {
                sb.append(ch);
            }
        }

        String result = sb.toString();
        String reversed = sb.reverse().toString();

        if (!result.equals(reversed)) {
            isPalindrome = false;
        }

        return Arrays.asList(result, isPalindrome);
    }
}

