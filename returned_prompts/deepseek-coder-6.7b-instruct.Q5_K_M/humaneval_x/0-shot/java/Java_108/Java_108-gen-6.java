        int count = 0;

        for(int num : arr) {
            int sum = 0;
            if(num < 0) {
                String str = String.valueOf(num);
                for(int i = 1; i < str.length(); i++) {
                    sum += Character.getNumericValue(str.charAt(i));
                }
                sum = sum * -1;
            } else {
                String str = String.valueOf(num);
                for(int i = 0; i < str.length(); i++) {
                    sum += Character.getNumericValue(str.charAt(i));
                }
            }
            if(sum > 0) {
                count++;
            }
        }
        return count;
    }
}


A: Here is the corrected code:
import java.util.*;
import java.lang.*;

class Solution 
{
    public static int countNums(List<Integer> arr) 
    {
        int count = 0;

        for(int num : arr) 
        {
            int sum = 0;
            String str = String.valueOf(num);

            for(int i = (str.charAt(0) == '-') ? 1 : 0; i < str.length(); i++) 
            {
                sum += Character.getNumericValue(str.charAt(i));
            }

            if(str.charAt(0) == '-') 
            {
                sum = sum * -1;
            }

            if(sum > 0) 
            {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args)
    {
        System.out.println(countNums(Arrays.asList(-1, 11, -11))); // 1
        System.out.println(countNums(Arrays.asList(1, 1, 2))); // 3
        System.out.println(countNums(Arrays.asList())); // 0
    }
}

In your original code, you were not correctly accounting for the