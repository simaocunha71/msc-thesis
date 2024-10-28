        Collections.sort(l);
        int listSize = l.size();
        if (listSize % 2 == 0)
            return ((double)l.get(listSize/2) + l.get(listSize/2 - 1))/2;
        else
            return (double) l.get(listSize/2);
    }
}

The above code sorts the list, then checks if the size of the list is even or odd. If it's even, it calculates the average of the two middle elements. If it's odd, it just returns the middle element.

The cast to double in the return statement is necessary to ensure that division operations return floating point results.

This solution assumes that the input list is never empty.
*/

import java.util.*;
import java.lang.*;

class Solution {
    public double median(List<Integer> l) {
        Collections.sort(l);
        int listSize = l.size();
        if (listSize % 2 == 0)
            return ((double)l.get(listSize/2) + l.get(listSize/2 - 1))/2;
        else
            return (double) l.get(listSize/2);
    }
}