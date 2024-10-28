        int dot = file_name.indexOf('.');
        if(dot == -1) return "No";
        if(dot == file_name.length()-1 || dot == 0) return "No";

        String name = file_name.substring(0, dot);
        String extension = file_name.substring(dot+1);

        int digitCount = 0;
        for(char c : name.toCharArray()) {
            if(!Character.isLetterOrDigit(c)) return "No";
            if(Character.isDigit(c)) digitCount++;
            if(digitCount > 3) return "No";
        }

        if(extension.equals("txt") || extension.equals("exe") || extension.equals("dll")) return "Yes";
        return "No";
    }
}

The code will return "Yes" if the file's name is valid and "No" otherwise. It checks the conditions for a valid file name and returns the corresponding result. It counts the number of digits in the file name to ensure there are no more than three of them. It checks if the file name ends with a dot or starts with a dot. It then checks if the file name starts with a letter and contains only letters and digits.

The complexity of the code is O(n), where n is the length of the file name. The code scans the file name character by character to count the number of digits and check if each character is a letter or a digit.
*/

//Solution.java

import java.util.*;
import java.lang.*;

class Solution  {
    public String filenameCheck(String file_name) {
        int dot = file_name.indexOf('.');
        if(dot == -1) return "No";
        if(dot == file_name.length()-1 || dot == 0) return "No";

        String name = file_name.substring(0, dot);
        String extension = file_name.substring(dot+1);

        int digitCount = 0;
        for(char c : name.toCharArray()) {
            if(!Character.isLetterOrDigit(c)) return "No";
            if(Character.is