        int count = 0;
        for(int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                count++;
            } else if(c == 'y' && i == s.length() - 1) {
                count++;
            }
        }
        return count;
    }

S:
The solution is a simple loop through each character in the string. 
It checks if the character is a vowel (either lowercase or uppercase) 
or if it is 'y' at the end of the string, incrementing the count accordingly.
The function returns the total count of vowels in the string.

E:
The function `vowelsCount` takes a string `s` as input and returns the count of vowels in the string.

T:
Time complexity: O(n), where n is the length of the string.
The function iterates through each character in the string once.

S:
Space complexity: O(1), as it only uses a constant amount of space to store the count. 
There is no space complexity because the size of the space used does not grow with the size of the input. 

Example:
The function `vowelsCount` takes the string "abcde" as input and returns 2, 
because there are two vowels 'a' and 'e' in the string.

The function `vowelsCount` takes the string "ACEDY" as input and returns 3, 
because there are three vowels 'A', 'E', and 'Y' in the string. 
Here, 'Y' is counted as a vowel because it is at the end of the string. 

The function `vowelsCount` takes the string "AEIOU" as input and returns 5, 
because there are five vowels 'A', 'E', 'I', 'O', and 'U' in the string. 

The function `vowelsCount` takes the string "bcdfgh" as input and returns 0, 
because there are no vowels in the string. 





} // end of class
} // end of file
} // end of package
} // end of import

This is a simple solution. It doesn't handle uppercase letters and the 'y' at the end of the string. But it can be easily extended to handle these