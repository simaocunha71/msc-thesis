        if  (isPalindrome(string)) {
            return string;
        }

        for  (int i = string.length() - 1; i >= 0; i--) {
            if  (isPalindrome(string.substring(0, i))) {
                String postfix 
                    = string.substring(i, string.length());
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


A: Here are the answers:

Q1:
>>> hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5)
false

Q2:
>>> hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3)
true

Q3:
>>> separateParenGroups("(  )  (( ))  (( )( ))")
["()", "(())", "(()())"]

Q4:
>>> truncateNumber(3.5)
0.5

Q5:
>>> makePalindrome("")
""

>>> makePalindrome("cat")
"catac"

>>> makePalindrome("cata")
"catac"

I hope this helps you in understanding the logic behind the code.

A: Here are the answers:

Q1:
>>> hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5)
false

Q2:
>>> hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3)
true

Q3:
>>> separateParenGroups("(  )  (( ))  (( )( ))")
["()", "(())",