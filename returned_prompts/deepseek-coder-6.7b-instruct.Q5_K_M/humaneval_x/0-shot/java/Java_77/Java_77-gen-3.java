        int i = 0;
        while (i * i * i <= Math.abs(a)) {
            if (i * i * i == Math.abs(a)) {
                return true;
            }
            i++;
        }
        return false;
    }
}

Explanation:
The function iscube takes an integer a as an argument. The while loop checks for each number i if i^3 equals the absolute value of a. If it finds such an i, it returns true, otherwise it returns false. Math.abs is used to handle negative numbers as they could also be cube roots of positive numbers.


Test Cases:
The function should pass the following test cases:

iscube(1) should return true
iscube(2) should return false
iscube(-1) should return true
iscube(64) should return true
iscube(0) should return true
iscube(180) should return false

*/



import java.util.*;
import java.lang.*;

class Solution {
    public boolean iscube(int a) {
        int i = 0;
        while (i * i * i <= Math.abs(a)) {
            if (i * i * i == Math.abs(a)) {
                return true;
            }
            i++;
        }
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.iscube(1)); // should print true
        System.out.println(s.iscube(2)); // should print false
        System.out.println(s.iscube(-1)); // should print true
        System.out.println(s.iscube(64)); // should print true
        System.out.println(s.iscube(0)); // should print true
        System.out.println(s.iscube(180)); // should print false
    }
}



```




































