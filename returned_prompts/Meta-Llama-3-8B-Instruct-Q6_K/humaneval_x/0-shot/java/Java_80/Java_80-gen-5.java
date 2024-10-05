        if(s.length() < 3)
            return false;

        for(int i = 0; i < s.length() - 2; i++) {
            String threeConsecutiveLetters = s.substring(i, i + 3);
            if(threeConsecutiveLetters.indexOf(threeConsecutiveLetters.charAt(0)) != threeConsecutiveLetters.indexOf(threeConsecutiveLetters.charAt(1)) 
                && threeConsecutiveLetters.indexOf(threeConsecutiveLetters.charAt(0)) != threeConsecutiveLetters.indexOf(threeConsecutiveLetters.charAt(2)) 
                && threeConsecutiveLetters.indexOf(threeConsecutiveLetters.charAt(1)) != threeConsecutiveLetters.indexOf(threeConsecutiveLetters.charAt(2)))
                continue;
            else
                return false;
        }
        return true;
    }
} 

Explanation:
This solution checks if a given string is "happy" or not. A string is considered "happy" if its length is at least 3 and every 3 consecutive letters are distinct. 

The isHappy() function takes a string s as input and returns a boolean value indicating whether the string is "happy" or not. 

If the length of the string is less than 3, it returns false because a string of length less than 3 cannot be "happy". 

Then, it iterates over the string using a for loop. For each substring of length 3, it checks if the three consecutive letters are distinct by comparing their indices in the substring. If the indices are the same, it means that the three letters are the same, and the function returns false. 

If the function does not return false after checking all substrings of length 3, it means that every 3 consecutive letters are distinct, and the function returns true. 

This solution has a time complexity of O(n), where n is the length of the string, because it iterates over the string once. The space complexity is O(1), which means that the space required does not change with the size of the input string, because it only uses a constant amount of space to store the indices and the substring. 

This solution assumes that the input string contains only lowercase English letters. If the input string can contain uppercase letters or other characters, the solution may need to be modified accordingly. 

The solution uses the substring() method to extract substrings of length 3 from the input string. It uses the indexOf() method to find the index of a character in a string. It uses the != operator to compare the