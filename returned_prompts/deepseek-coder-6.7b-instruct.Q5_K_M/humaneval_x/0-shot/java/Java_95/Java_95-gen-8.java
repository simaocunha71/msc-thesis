        boolean lower = true;
        boolean upper = true;
        for(Map.Entry<Object, Object> entry: dict.entrySet()){
            if(!(entry.getKey() instanceof String)){
                return false;
            }
            if(((String)entry.getKey()).equals(((String)entry.getKey()).toLowerCase())){
                lower = false;
            }
            if(((String)entry.getKey()).equals(((String)entry.getKey()).toUpperCase())){
                upper = false;
            }
        }
        if(lower == true && upper == true && dict.size()>0){
            return false;
        }
        return true;
    }
}


A: There is a small mistake in the if conditions. You should check if the key is in lower or upper case, not if it equals to the lower or upper case version of itself.
Here is the corrected code:
import java.util.*;
import java.lang.*;

class Solution  {
    public boolean checkDictCase(Map<Object, Object> dict)  {
        boolean lower = true;
        boolean upper = true;
        for(Map.Entry<Object, Object> entry: dict.entrySet()){
            if(!(entry.getKey() instanceof String)){
                return false;
            }
            if(!(((String)entry.getKey()).equals(((String)entry.getKey()).toLowerCase()))){
                lower = false;
            }
            if(!(((String)entry.getKey()).equals(((String)entry.getKey()).toUpperCase()))){
                upper = false;
            }
        }
        if(lower && upper && !dict.isEmpty()){
            return false;
        }
        return true;
    }
}

In this code, the if conditions are corrected to check if the key is in lower or upper case, not if it equals to the lower or upper case version of itself. Also, I replaced dict.size()>0 with !dict.isEmpty() to check if the dictionary is not empty.

A: Here's the corrected code:

import java.util.*;
import java.lang.*;

class Solution {
