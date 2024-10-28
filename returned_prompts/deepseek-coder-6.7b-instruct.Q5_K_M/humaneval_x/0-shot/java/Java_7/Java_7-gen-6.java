    List<String> result = new ArrayList<>();

    for(String str : strings){
        if(str.contains(substring)){
            result.add(str);
        }
    }

    return result;
    }
}


A: You are on the right track, but you should be using the built-in method "contains()" of the String class, which checks whether a string contains a specified sequence of char values.

Here is the corrected code:
import java.util.*;

class Solution {
    
    public List<String> filterBySubstring(List<String> strings, String substring) {
        List<String> result = new ArrayList<>();

        for(String str : strings){
            if(str.contains(substring)){
                result.add(str);
            }
        }

        return result;
    }
}

This code takes a list of strings and a substring as input, checks each string in the list to see if it contains the given substring, and if it does, adds it to the result list. Finally, it returns the result list.

A: import java.util.*;

class Solution {
    
    public List<String> filterBySubstring(List<String> strings, String substring) {
        List<String> result = new ArrayList<>();

        for(String str : strings){
            if(str.contains(substring)){
                result.add(str);
            }
        }

        return result;
    }
}

This solution works perfectly. This code takes a list of strings and a substring as input, checks each string in the list to see if it contains the given substring, and if it does, adds it to the result list. Finally, it returns the result list.

A: Here is the corrected code:
import java.util.*;

class Solution {
    
    public List<String> filterBySubstring(List<String> strings, String substring) {
        List<String> result = new ArrayList<>();

        for(String str : strings){
            if(str.contains(substring)){
                result.add(str);
            }
        }

        return result;
   