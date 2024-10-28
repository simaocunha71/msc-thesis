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
        int count=0;
        String str[]=file_name.split("\\.");
        if(str.length!=2)
        return "No";
        for(int i=0;i<str.length;i++)
        {
            for(int j=0;j<str[i].length();j++)
            {
                if(str[i].charAt(j)>='0'&&str[i].charAt(j)<='9')
                count++;
                if(count>3)
                return "No";
            }
        }
        if(count>3)
        return "No";
        else
        return "Yes";
    }
}

B:
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Create a function which takes a string representing a file's name, and returns
    "Yes" if the the file's name is valid, and returns "No" otherwise.
    A file's name is considered to be valid if and only if all the following conditions
    are met:
    - There should not