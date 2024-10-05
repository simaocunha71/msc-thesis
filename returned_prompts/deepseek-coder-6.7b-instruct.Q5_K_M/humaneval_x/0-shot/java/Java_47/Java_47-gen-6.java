        int n = l.size();
        if(n == 0) {
            throw new IllegalArgumentException("List is empty");
        }
        Collections.sort(l);
        if(n % 2 == 0) {
            return (l.get(n/2) + l.get(n/2 - 1)) / 2.0;
        } else {
            return l.get(n/2);
        }
    }
}

I:
import java.util.*;
import java.lang.*;

class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution sol = new Solution();
        System.out.println(sol.median(Arrays.asList(3, 1, 2, 4, 5)));
        System.out.println(sol.median(Arrays.asList(-10, 4, 6, 1000, 10, 20)));
    }
}

O:
3
15.0
*/

