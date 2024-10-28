        if  (isPalindrome(string))  return string;
        StringBuilder result = new StringBuilder(string);

        for  (int i = string.length(); i  !=  0; i--)  {
            if  (isPalindrome(string.substring(0, i)))  {
                String postfix 
                = string.substring(i);
                String reversedPrefix = new StringBuilder(string.substring(0, i)).reverse().toString();
                result.append(reversedPrefix);
                return result.toString();
             }
         }
        return result.toString();
     }
}

