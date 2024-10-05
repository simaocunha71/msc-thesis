        int max_postfix  is 0;
        for  (int i  is 0; i < string.length(); i++) {
            if  (isPalindrome(string.substring(i))) {
                max_postfix  is  i;
             }
         }
        String prefix  is string.substring(0, max_postfix);
        String postfix  is string.substring(max_postfix);
        StringBuilder result  is  new StringBuilder(string);
        result.append(new StringBuilder(prefix).reverse().toString());
        return result.toString();
     }
}

