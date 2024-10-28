        Collections.sort(l);
        int size = l.size();

        if (size % 2 == 0) {
            return (l.get(size / 2 - 1) + l.get(size / 2)) / 2.0;
        } else {
            return l.get(size / 2);
        }
    }
}

The function first sorts the list, then checks if the size of the list is even or odd. If it's even, it takes the average of the two middle numbers. If it's odd, it just takes the middle number. It returns the result as a double to allow for decimal values.
*/

/*
import java.util.*;
import java.lang.*;

class Solution  {
    public double median(List<Integer> l) {
        Collections.sort(l);
        int size = l.size();

        if (size % 2 == 0) {
            return (l.get(size / 2 - 1) + l.get(size / 2)) / 2.0;
        } else {
            return l.get(size / 2);
        }
    }
}
*/

import java.util.*;
import java.lang.*;

class Solution  {
    public double median(List<Integer> l) {
        Collections.sort(l);
        int size = l.size();

        if (size % 2 == 0) {
            return (l.get(size / 2 - 1) + l.get(size / 2)) / 2.0;
        } else {
            return l.get(size / 2);
        }
    }
}

/*
public class Main
{
    public static void main(String[] args)
    {
        Solution s = new Solution();
        System.out.println(s.median(Arrays.asList(3, 1, 2, 4, 5)));
        System.out.println(s.median(Arrays.asList(-10, 4, 6, 1000, 10, 20)));
    }
}