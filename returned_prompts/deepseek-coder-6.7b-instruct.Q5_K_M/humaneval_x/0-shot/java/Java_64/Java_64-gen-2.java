        int count = 0;
        String lower = s.toLowerCase();

        for(int i = 0; i < s.length(); i++){
            char c = lower.charAt(i);
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

This code converts the input string to lowercase so it doesn't matter if the input is in upper or lower case. It then checks each character in the string to see if it is a vowel. If it is, it increments the count variable. If the last character of the string is 'y', it also increments the count variable. Finally, it returns the count variable which is the number of vowels in the string.

This code does not handle inputs that are not strings or are null. It is assumed that the input will always be a valid string.

Note: The time complexity of this solution is O(n), where n is the length of the string. This is because it iterates through the string once. The space complexity is O(1), as it only uses a constant amount of space to store the count and the string.
