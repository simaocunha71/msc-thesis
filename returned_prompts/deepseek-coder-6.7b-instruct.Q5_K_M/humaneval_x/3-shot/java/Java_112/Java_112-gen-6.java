        StringBuilder result = new StringBuilder();
        for(char ch : s.toCharArray()){
            if(!c.contains(String.valueOf(ch))){
                result.append(ch);
            }
        }
        boolean isPalindrome = result.toString().equals(result.reverse().toString());
        result.reverse();
        return Arrays.asList(result.toString(), isPalindrome);
    }
}

