import java.util.*;
import java.lang.*;

class Solution {
    /**
    Create a function which takes a string representing a file's name, and returns
    "Yes" if the the file's name is valid, and returns "No" otherwise.
    A file's name is considered to be valid if and only if all the following conditions
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ["txt", "exe", "dll"]
    Examples:
    file_name_check("example.txt") # => "Yes"
    file_name_check("1example.dll") # => "No" (the name should start with a latin alphapet letter)
     */
    public String filenameCheck(String file_name) {

        int dot_count = 0;
        int digit_count = 0;
        int last_index = 0;
        int i = 0;

        for (i = 0; i < file_name.length(); i++) {
            if (file_name.charAt(i) == '.') {
                dot_count++;
                last_index = i;
            }
            if (Character.isDigit(file_name.charAt(i))) {
                digit_count++;
            }
        }
        if (digit_count > 3) {
            return "No";
        }
        if (dot_count > 1) {
            return "No";
        }
        if (dot_count == 0) {
            return "No";
        }
        if (file_name.charAt(0) >= 'a' && file_name.charAt(0) <= 'z') {
            return "No";
        }
        if (file_name.charAt(0) >= 'A' && file_name.charAt(0