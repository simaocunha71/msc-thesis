        if  (string.equals("")) return "";

        int end  index = string.length();
        while  (end  index  > 0  &&  !isPalindrome(string.substring(0, end  index))) end  index --;

        if  (end  index  == string.length()) return string;

        String suffix  palindrome = string.substring(end  index);
        String prefix  non  palindrome = string.substring(0, end  index);
        String prefix  reverse = new StringBuilder(prefix).reverse().toString();
        return string + prefix  reverse;
     }
}

