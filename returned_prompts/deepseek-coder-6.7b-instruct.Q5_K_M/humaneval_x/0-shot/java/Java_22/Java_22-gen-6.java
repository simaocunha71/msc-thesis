Here is the corrected code:

import java.util.*;
import java.lang.*;

class Solution 
{
    public List<Integer> filterIntegers(List<Object> values) 
    {
        List<Integer> intList = new ArrayList<Integer>();

        for (Object obj : values) 
        {
            if (obj instanceof Integer) 
            {
                intList.add((Integer) obj);
            }
        }

        return intList;
    }
}

