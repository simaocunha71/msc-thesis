```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean simplify(String x, String n) {
        int num_x = Integer.parseInt(x.split("/")[0]);
        int den_x = Integer.parseInt(x.split("/")[1]);
        int num_n = Integer.parseInt(n.split("/")[0]);
        int den_n = Integer.parseInt(n.split("/")[1]);

        int num_res = num_x * num_n;
        int den_res = den_x * den_n;

        return num_res % den_res == 0;
    }
}
```