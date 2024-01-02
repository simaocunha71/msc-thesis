import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return list of all prefixes from shortest to longest of the input string
    >>> allPrefixes("abc")
    ["a", "ab", "abc"]
     */
    public List<String> allPrefixes(String string) {
        List<String> result = new ArrayList<>();
        
        if (string == null || "".equals(string)) return result;
        
        for(int i=0 ; i<=string.length() ; ++i){
            String prefix = string.substring(0, i);
            
            if(prefix.isEmpty()) continue;
            
            result.add(prefix);
        }
        Collections.sort(result); 
        
        return result;
    }
}