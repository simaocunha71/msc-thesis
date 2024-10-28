import java.util.*;

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

        int count = 0;
        for (int i = 0; i < file_name.length(); i++) {
            if (file_name.charAt(i) >= '0' && file_name.charAt(i) <= '9') {
                count++;
            }
            if (count > 3) {
                return "No";
            }
        }

        String[] temp = file_name.split("\\.");
        if (temp.length != 2) {
            return "No";
        }

        if (temp[0].length() == 0 || !(temp[0].charAt(0) >= 'a' && temp[0].charAt(0) <= 'z' || temp[0].charAt(0) >= 'A' && temp[0].charAt(0) <= 'Z')) {
            return "No";
        }

        if (!(temp[1].equals("exe") || temp[1].equals("dll") || temp[1].equals("txt"))) {
            return "No";
        }

        return "Yes";
    }