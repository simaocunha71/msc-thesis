        int counter = 0;

        for (int i = 0; i < string.length(); i++) {
            if (string.substring(i).startsWith(substring)) {
                counter++;
                continue A;
            }
        }
        return counter;
    }
}



public class Main {
    public static void main(String[] args) {
        System.out.println(new Solution().howManyTimes("aaa", "a"));
    }
}




```

```
import java.util.*;
import java.lang.*;

class Solution {
    public int howManyTimes(String string, String substring) {
        int counter = 0;
        int i = 0;
        while (i < string.length()) {
            if (string.substring(i).startsWith(substring)) {
                counter++;
                i += substring.length();
                continue;
            }
            i++;
        }
        return counter;
    }
}
```

```
import java.util.*;
import java.lang.*;

class Solution {
    public int howManyTimes(String string, String substring) {
        int counter = 0;
        for (int i = 0; i < string.length(); i++) {
            if (string.substring(i).startsWith(substring)) {
                counter++;
                i += substring.length();
                continue;
            }
        }
        return counter;
    }
}
```

```
import java.util.*;
import java.lang.*;

class Solution {
    public int howManyTimes(String string, String substring) {
        int counter = 0;
        int i = 0;
        while (i < string.length()) {
            if (string.substring(i).startsWith(substring)) {
                counter++;
                i += substring.length();
                continue;
            }
            i++;
        }
        return counter;
    }
}
```
```

```

```

```

```

```
