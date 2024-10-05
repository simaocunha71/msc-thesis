        StringBuilder sb = new StringBuilder();
        boolean isPalindrome = false;
        for(char ch : s.toCharArray()) {
            if(!c.contains(String.valueOf(ch))) {
                sb.append(ch);
            }
        }
        String result = sb.toString();
        String reverseResult = sb.reverse().toString();
        if(result.equals(reverseResult)) {
            isPalindrome = true;
        }
        return Arrays.asList(result, isPalindrome);
    }
}

