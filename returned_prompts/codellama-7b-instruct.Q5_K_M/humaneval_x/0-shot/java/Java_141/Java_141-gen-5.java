import java.util.*;
import java.lang.*;

class Solution {
    public String filenameCheck(String file_name) {
        int count = 0;
        for(int i = 0; i < file_name.length(); i++){
            if(file_name.charAt(i) >= '0' && file_name.charAt(i) <= '9'){
                count++;
            }
        }
        if(count > 3){
            return "No";
        }
        if(file_name.contains(".")){
            if(file_name.charAt(file_name.indexOf(".") - 1) == '.'){
                return "No";
            }
        }
        if(file_name.charAt(0) >= 'a' && file_name.charAt(0) <= 'z' && file_name.charAt(0) >= 'A' && file_name.charAt(0) <= 'Z'){
            if(file_name.substring(file_name.indexOf(".") + 1).equals("txt") || file_name.substring(file_name.indexOf(".") + 1).equals("exe") || file_name.substring(file_name.indexOf(".") + 1).equals("dll")){
                return "Yes";
            }
        }
        return "No";
    }
}

