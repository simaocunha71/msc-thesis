        if  (isPalindrome(string))  {
            return string;
         }
        for  (int i = string.length(); i >= 0; i--)  {
            if  (isPalindrome(string.substring(0, i)))  {
                String postfix 
                = string.substring(i);
                String prefix 
                = string.substring(0, i);
                StringBuilder result 
                = new StringBuilder(string);
                result.append(new StringBuilder(postfix).reverse().toString());
                return result.toString();
             }
         }
        return null;
     }
}

