import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return maximum element in the list.
    >>> maxElement(Arrays.asList(1, 2, 3))
    3
    >>> maxElement(Arrays.asList(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10))
    123
     */
    public int maxElement(List<Integer> l) {

### 1. 코드를 작성합니다.

```java
class Solution {
    public int maxElement(List<Integer> l) {
        int max = Integer.MIN_VALUE;
        for(int i : l) {
            if(i > max) {
                max = i;
            }
        }
        return max;
    }
}
```

### 2. 정답 및 메모를 확인합니다.

![](/assets/img/post/2020-02-27-15-49-03.png)

![](/assets/img/post/2020-02-27-15-50-06.png)

### 3. 다른 사람 풀이를 확인합니다.

![](/assets/img/post/2020-02-27-15-50-38.png)

![](/assets/img/post/2020-02-27-15-51-00.png)

![](/assets/img/post/2020-02-27-15-51-03.png)

![](/assets/img/post/2020-02-27-15-51-06.png)

![](/assets/img/post/2020-02-27-15-51-09.png)

![](/assets/img