    float max = -INFINITY;
    for(int i = 0; i<l.size(); i++){
        if(l[i] > max){
            max = l[i];
        }
    }
    return max;
}

int main(){
    vector<float> l = {5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10};
    printf("%f\n", max_element(l));
    return 0;
}

*/

#include<bits/stdc++.h>
using namespace std;

int max_element(vector<int> l){
    int max = -1e9;
    for(int i = 0; i<l.size(); i++){
        if(l[i] > max){
            max = l[i];
        }
    }
    return max;
}

int main(){
    vector<int> l = {5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10};
    printf("%d\n", max_element(l));
    return 0;
}
```

### Python

```python
def max_element(l):
    return max(l)
```

### JavaScript

```javascript
function max_element(l){
    return Math.max(...l);
}
```

### Java

```java
import java.util.Collections;
import java.util.List;

public static int max_element(List<Integer> list) {
    return Collections.max(list);
}
```

### C++

```c++
#include <algorithm>
#include <vector>

int max_element(std::vector<int>& v) {
    return *max_element(v.begin(), v.end());
}
```

### Ruby

```ruby
def max_element(l)
    l.max
end
```

### PHP

```php
function max_element($l) {
   