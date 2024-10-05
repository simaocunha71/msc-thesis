        if(x instanceof Integer && y instanceof Integer && z instanceof Integer){
            int sum = (Integer)x + (Integer)y;
            if(sum == (Integer)z || (Integer)x == sum || (Integer)y == sum || (Integer)z == sum){
                return true;
            }
        }
        return false;
    }
}

The function should take three objects as parameters because the requirements specify that the input can be any type (Integer or not). The function checks whether each object is an instance of Integer, then it adds the first two integers and checks if the sum is equal to the third integer. If so, it returns true; otherwise, it returns false.

Please note that this solution assumes that the inputs are integers. If you want to allow for non-integer inputs, you would need to modify the function to handle non-integer inputs appropriately.
*/

import java.util.*;
import java.lang.*;

class Solution  {
    public boolean anyInt(Object x, Object y, Object z)  {
        if(x instanceof Integer && y instanceof Integer && z instanceof Integer){
            int sum = (Integer)x + (Integer)y;
            if((Integer)z == sum || (Integer)x == sum || (Integer)y == sum){
                return true;
            }
        }
        return false;
    }
}

public class Main
{
    public static void main (String[] args) throws java.lang.Exception
    {
        Solution s = new Solution();
        System.out.println(s.anyInt(5, 2, 7)); // Output: true
        System.out.println(s.anyInt(3, 2, 2)); // Output: false
        System.out.println(s.anyInt(3, -2, 1)); // Output: true
        System.out.println(s.anyInt(3.6, -2.2, 2)); // Output: false
    }
}

```

This is a solution for the problem. This function will return true if one of the numbers is equal to the sum of the other two, and all numbers are integers. If not, it will return false.

The function takes three objects as parameters and