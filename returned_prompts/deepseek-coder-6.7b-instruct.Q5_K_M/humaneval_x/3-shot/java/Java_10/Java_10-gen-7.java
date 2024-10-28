        if  (isPalindrome(string)) 
            return string;

        StringBuilder reverseString = new StringBuilder(string).reverse();
        String tempString;

        for  (int i = string.length(); i >= 0; i--)  {
            tempString = string + reverseString.substring(string.length()-i);

            if  (isPalindrome(tempString)) 
                return tempString.toString();
        }
        return null;
     }
}

