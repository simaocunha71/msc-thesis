        if  (string.equals(""))  return "";
        int longest_palindromic_suffix = string.length();
        for  (; longest_palindromic_suffix > 0;  longest_palindromic_suffix--)  {
            if  (isPalindrome(string.substring(0, longest_palindromic_suffix)))  break;
         }
        String prefix = string.substring(0, longest_palindromic_suffix);
        String postfix = string.substring(longest_palindromic_suffix, string.length());
        StringBuilder result = new StringBuilder(string);
        result.append(new StringBuilder(prefix).reverse().toString());
        return result.toString();
     }
}

