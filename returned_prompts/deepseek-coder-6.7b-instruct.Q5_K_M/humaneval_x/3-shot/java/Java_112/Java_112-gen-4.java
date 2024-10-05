        StringBuilder sb = new StringBuilder();

        for(char ch : s.toCharArray()) {
            if(!c.contains(String.valueOf(ch))) {
                sb.append(ch);
            }
        }

        String result = sb.toString();
        boolean isPalindrome = result.equals(new StringBuilder(result).reverse().toString());

        return Arrays.asList(result, isPalindrome);
    }
}

