import java.util.*;
import java.lang.*;

class Solution {
    /**
    Filter an input list of strings only for ones that contain given substring
    >>> filterBySubstring(List.of(), "a")
    []
    >>> filterBySubstring(Arrays.asList("abc", "bacd", "cde", "array"), "a")
    ["abc", "bacd", "array"]
     */
    public List<String> filterBySubstring(List<String> strings, String substring) {
        Map<String, Boolean> map = new HashMap<>();
        for (String s : strings){
            // Add each string to the map if any of its characters match 
            for (char c:s.toCharArray()){
                map.put(String.valueOf(c), true);
            }
        }
        
        List<String> result = new ArrayList<>();
        for(String s : strings){
            if(map.containsKey(substring)){
                // The substring should be part of the string
                result.add(s);
            }
        }
        return Collections.unmodifiableList(result);
    }
}