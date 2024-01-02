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
        if(!file_name.contains(".") || !file_name.startsWith("\\"))  return "No";
        
        StringBuilder sb = new StringBuilder();
        List<Character> characters = Arrays.asList("0", "1", "2", "3", "4", "5", "6", "7", "8", "9");
        for(int i=0; i < file_name.length(); i++){
            char c = (char)file_name.charAt(i);
            if(!Character.isLetterOrDigit(c)){
                sb.append("Error! File name should start with a letter or digit"); return "No";
            }
            
            if(!characters.contains(c)) {
                sb.append("Error! Filename should not contain more than three digits"); return "No"; 
            }
        }
        
        String sub_before = file_name.substring(0,file_name.indexOf("."));
        if(!StringUtils.containsLetters(sub_before)) {
            sb.append("Error! Filename should start with a letter or