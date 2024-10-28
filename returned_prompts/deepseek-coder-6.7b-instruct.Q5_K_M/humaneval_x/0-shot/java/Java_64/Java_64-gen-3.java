        int count = 0;
        String lowerCase = s.toLowerCase();

        for(int i = 0; i < s.length(); i++){
            char c = lowerCase.charAt(i);
            if( c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
                count++;
            }
        }
        if(s.charAt(s.length()-1) == 'y'){
            count++;
        }
        return count;
    }
}

The function starts by setting a counter to 0, then it converts the string to lowercase.
After that, it iterates through the characters in the string. If the character is a vowel (either 'a', 'e', 'i', 'o', 'u'), the counter is incremented.
Finally, it checks if the last character in the string is 'y'. If it is, the counter is incremented. The final count is then returned.

*/

// Test Cases:
// "abcde" should return 2
// "ACEDY" should return 3
// "y" should return 1
// "Y" should return 1
// "aeiou" should return 5
// "bcdfghjklmnpqrstvwxyz" should return 0
// "AEIOU" should return 5
// "bcdfghjklmnpqrstvwxy" should return 1
// "YyYy" should return 4
// "bcdfghjklmnpqrstvwxyY" should return 2
// "bcdfghjklmnpqrstvwxyYyY" should return 3
// "bcdfghjklmnpqrstvwxyYyYy" should return 4
// "bcdfghjklmnpqrstvwxyYyYyY" should return 5
// "bcdfghjklmnpqrstvwxyYyYyYy" should return 6
// "bcdfghjklmnpqrstvwxyYyYyY